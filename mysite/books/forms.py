# -*- coding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    subject  = forms.CharField(max_length=50)
    email = forms.EmailField(required=False,label='You E-mail')
    message = forms.CharField(widget=forms.Textarea,max_length=200)

    def clean_message(self):
        message  = self.cleaned_data['message']
        num_word  = len(message.split())
        if num_word < 2:
            raise forms.ValidationError('Not enough words!')
        return  message