from django.forms import ModelForm
from Cv.models import Profile
from django import forms

class formule(ModelForm):
    class Meta:
        model=Profile
        fields=['image', 'name','username','email','phone','address','competance','langue','interet','qualite','profile','experience','education','Projet']


class Fprofile(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={


            'class':'c2'
        }
    ))
    name = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'votre nom ici...',

            'class':'c2'
        }
    ))
    username = forms.CharField(label='',required=False,widget=forms.TextInput(
        attrs={
            'placeholder':'votre prenom ici...',

            'class':'c2'
        }
    ))
    email = forms.EmailField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'votre email ici...',

            'class':'c2'
        }
    ))
    phone = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'votre numero de telephone ici...',

            'class':'c2'
        }
    ))
    address = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'votre address ici...',

            'class':'c2'
        }
    ))
    langue = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'vos langue parler ici...',

            'class':'c2'
        }
    ))
    competance = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'votre competance ici...',

            'class':'c1'
        }
    ))

    '''interet = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'vos interet ici',

            'class':'c2'
        }
    ))'''
    qualite = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'vos qualité ici ...',

            'class':'c1'
        }
    ))
    profile = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'votre profile ici ...',

            'class':'c1'
        }
    ))
    experience =forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'votre experience ici ...',

            'class':'c1'
        }
    ))
    education = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'votre  education ici ...',

            'class':'c1'
        }
    ))
    Projet = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder':'votre projet ici ...',

            'class':'c1'
        }
    ))