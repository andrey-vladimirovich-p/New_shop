from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput




class ContactForm(forms.Form):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    subject = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Тема', 'class': 'form-control'}))
    content = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder': 'Введите текст сообщения', 'rows': 6, 'class': 'form-control'}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'},)