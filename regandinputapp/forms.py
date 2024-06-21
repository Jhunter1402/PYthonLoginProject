from django import forms
class RegForm(forms.Form):
    FirstName = forms.CharField(max_length=15)
    LastName = forms.CharField(max_length=15)
    UserName = forms.CharField(max_length=15)
    Password = forms.CharField(max_length=15, widget=forms.PasswordInput())
    CPassword = forms.CharField(max_length=15, widget=forms.PasswordInput())
    EmailID = forms.EmailField()
    MobileNo = forms.IntegerField()
class LoginForm(forms.Form):
    UserName = forms.CharField(max_length=15)
    Password = forms.CharField(max_length=15, widget=forms.PasswordInput())