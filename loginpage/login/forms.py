from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'id':'user','class':'field','placeholder':'  Username'}))
    password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'id':'pass','class':'field','placeholder':'  Password'}))
class CreateForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'id': 'email_id', 'class': 'cfield', 'placeholder': '   email'}))
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'id':'cuser','class':'cfield','placeholder':'  username'}))
    password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'id':'cpass','class':'cfield','placeholder':'    password'}))
    conform_password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'id': 'ccpass', 'class': 'cfield', 'placeholder': '    conform password'}))
class ForgetPassword(forms.Form):
    email=forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={'id':'femail','class':'ffield','placeholder':'   email'}))
class VerifyPassword(forms.Form):
    password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'id':'vpass','class':'vfield','placeholder':'   New Password'}))
    conform_password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'id':'vcpass','class':'vfield','placeholdet':'   Conform Password'}))

