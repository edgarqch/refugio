from __future__ import absolute_import
from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = "__all__"
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_Aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_Aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }