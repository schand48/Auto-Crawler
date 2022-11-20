# Written by: Sumi
# Tested by:
# Debugged by:

from django import forms

class QueryForm(forms.Form):
    user_query = forms.CharField(label='Your search', max_length=255)