from allauth.account.forms import SignupForm
from django import forms

from django.contrib.auth import (
    get_user_model,
    authenticate,
)

# from .models import PerfilPF
# from .utils.Validator_CPF import CPF

User = get_user_model()


class userForm(forms.ModelForm):
    username =  forms.CharField(label='Usuário', max_length='14', required=True)
    first_name =  forms.CharField(label='Primeiro Nome', max_length='30', required=True)
    last_name =  forms.CharField(label='Último Nome', max_length='40', required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class perfilForm(forms.ModelForm):
    cpf         = forms.CharField(label='CPF', max_length='14', required=True)
    mobile      = forms.CharField(label='Celular', max_length='15', required=True)

    def clean_cpf(self):
        # Check that the two password entries match
        cpf = self.cleaned_data.get("cpf")
        cpf = CPF(cpf)
        print(cpf)
        valid = cpf.isValid()
        print(valid)
        if valid != True:
            raise forms.ValidationError("CPF inválido")
        return cpf

        # if check = :
        #     raise forms.ValidationError("Emails não coincidem")
        # return email
        # print("CPF é: " + ckeck)
    class Meta:
        model = PerfilPF
        fields = [
            # 'owner',
            'cpf',
            'mobile',
        ]
    def save(self, commit=True):
        # Save the provided password in hashed format
        form = super(PerfilPF, self).save(commit=False)
        if commit:
            form.save()
        return form