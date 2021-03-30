from django import forms
from django.forms import ModelForm
from .models import administracion



class formularioForm(ModelForm):
  class Meta:
    model=administracion
    fields='__all__'

