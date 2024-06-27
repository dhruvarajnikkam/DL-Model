from django import forms
from core.models import *



class FarmVideoUploadForm(forms.ModelForm):
    class Meta:
        model = FarmVideo
        fields = ("video","ph_farm","moisture_farm","temperature","total_amt_salt")
