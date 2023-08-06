import hashlib
import uuid
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string

from .defaults import (
    PASSWORDLESS_HASH_SALT,
    PASSWORDLESS_OTP_DICTIONARY,
    PASSWORDLESS_OTP_LENGTH,
    PASSWORDLESS_USE_CELERY,
)
from .tasks import celery_send_email


class AuthRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(db_index=True, editable=False)
    hash = models.CharField(
        max_length=64,
        db_index=True,
        blank=True,
        null=True,
        editable=False,
    )
    otp = models.CharField(max_length=24, blank=True, null=True, editable=False)
    email_sent = models.BooleanField(default=False, editable=False)
    is_used = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def create_otp(self):
        otp_length = getattr(
            settings,
            "PASSWORDLESS_OTP_LENGTH",
            PASSWORDLESS_OTP_LENGTH,
        )
        dictionary = getattr(
            settings,
            "PASSWORDLESS_OTP_DICTIONARY",
            PASSWORDLESS_OTP_DICTIONARY,
        )

        otp = []
        while len(otp) < otp_length:
            otp.append(dictionary[randint(0, len(dictionary) - 1)])

        return "".join(otp)

    def create_hash(self):
        salt = getattr(
            settings,
            "PASSWORDLESS_HASH_SALT",
            PASSWORDLESS_HASH_SALT,
        )

        plaintxt = ":".join(["djangopasswordless", self.email, salt])
        return hashlib.sha256(plaintxt.encode()).hexdigest()

    def public_hash(self):
        return f"{self.hash}{self.id}".replace("-", "").lower()

    def send_otp(self):
        context = {
            "email": self.email,
            "hash": self.public_hash(),
            "otp": self.otp,
        }

        send_mail(
            render_to_string(
                "passwordless/email/subject.txt",
                context=context,
            ),
            render_to_string(
                "passwordless/email/message.txt",
                context=context,
            ),
            None,
            [self.email],
            html_message=render_to_string(
                "passwordless/email/message.html",
                context=context,
            ),
            fail_silently=False,
        )

        self.email_sent = True
        self.save()

    def save(self, *args, **kwargs):
        if self.otp is None:
            self.otp = self.create_otp()

        if self.hash is None:
            self.hash = self.create_hash()

        super(AuthRequest, self).save(*args, **kwargs)

        if not self.email_sent:
            use_celery = getattr(
                settings,
                "PASSWORDLESS_USE_CELERY",
                PASSWORDLESS_USE_CELERY,
            )

            if use_celery:
                celery_send_email.delay(self.id)
            else:
                self.send_otp()


class AuthFailure(models.Model):
    hash = models.CharField(max_length=64, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
