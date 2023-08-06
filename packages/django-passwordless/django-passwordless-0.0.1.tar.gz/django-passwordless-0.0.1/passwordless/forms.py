from django import forms


class PasswordlessLoginForm(forms.Form):
    email = forms.EmailField()


class PasswordlessOTPForm(forms.Form):
    otp = forms.CharField(max_length=24)
