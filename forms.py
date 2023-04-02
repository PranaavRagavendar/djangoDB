from django import forms
from .models import Member,Login

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['staffname','subject','name1','name2','name3']
        
        
class LoginForm(forms.ModelForm):
    
    class Meta:
        model =  Login
        fields = ['email','password']