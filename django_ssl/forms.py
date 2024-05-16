from django import forms

class SearchForm(forms.Form):
    serial = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter Serial No',
        'style': 'height: 65px; width: 600px; background-color: #11191F; color: #616F78; font-size: 1.2rem;'
                 'margin-top: 30px; margin-bottom: 30px; padding-left: 20px; border-radius: 5px;',
        'onmouseover': "this.style.border='1px solid white'",
        'onmouseout': "this.style.border='0'",
    }))