from django import forms

class LoginForms(forms.Form):
    nomeUsuario = forms.CharField(
        # TODO - Form
    )
    senha = forms.PasswordInput()