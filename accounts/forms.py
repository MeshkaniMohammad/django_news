from django import forms



class UserForm(forms.Form):
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)

