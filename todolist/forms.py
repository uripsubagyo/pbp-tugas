from django import forms

class taskForm(forms.Form):
    titles = forms.CharField(widget=forms.TextInput(attrs={'name':'title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'name':'body'}))
    
