import django.forms as forms
from django.core.validators import EmailValidator, URLValidator

from .models import History
from .validators import validate_login, ValidationError

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.Form):
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='nazwisko')
    email = forms.CharField(label='Email', validators=[EmailValidator()])
    favourite_site = forms.CharField(label='Strona www', validators=[URLValidator()])


class AddUserForm(forms.Form):
    login = forms.CharField(label='Nazwa użytkownika', validators=[validate_login])
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    passwordTwo = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    email = forms.CharField(label='Email', validators=[EmailValidator()])

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['passwordTwo']:
            raise ValidationError('Wpisane hasła nie są takie same.')
        return cleaned_data

class HistoryModelForm(forms.ModelForm):
    class Meta:
        model = History
        exclude = ['date_sent']
