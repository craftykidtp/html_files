from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email address",
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address"}),
    )

    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "Choose a username"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Create a password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Enter the password again"})
