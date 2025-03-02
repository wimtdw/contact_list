from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile']
        widgets = {
            'email': forms.EmailInput(attrs={'type': 'email'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile.isdigit() or len(mobile) != 11:
            raise forms.ValidationError("Неверный формат номера телефона")
        return mobile
