from django.forms import ModelForm
from .models import User
from django.forms.widgets import PasswordInput, TextInput
from django.core.mail import send_mail


class RegisterForm(ModelForm):

    def send_message(self):
        pass

    class Meta:
        model = User
        fields = ['username','email','password','age','gender','icon']
        widgets = {
            'password': PasswordInput(attrs={'placeholder': '请输入密码'}, render_value=True),
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'emial': TextInput(attrs={'placeholder': '输入邮箱'}),
            'password': PasswordInput(attrs={'placeholder': '请输入密码'}, render_value=True)
        }
