from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from coneval_proyecto.models import *


# Aqui se definen las variable que se pondran en el formulario, en templates se le da el formato en html de como se presentaran estas variables.
class ConevalProyectoForm(forms.ModelForm):

    class Meta:
        model = ConevalProyectoModel

        fields = [
                "state",
        ]
        labels = {
            "Selecciona la entidad",
        }
        widgets = {
            "state":forms.Select(),
        }

