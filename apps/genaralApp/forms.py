from django import forms
from.models import Post
from captcha.fields import ReCaptchaField

class Postform(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Post
        fields= [
            'Name',
            'SurName',
            'Comment',
        ]
