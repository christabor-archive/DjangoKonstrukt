from django.db import models as _models
from django import forms
import models
import inspect


# Hax, inspect ftw
# Get the args and varargs of a given module
# for use in the form.
DJANGO_FIELD_ARGS = (
    (str(name), str(inspect.getargspec(obj.__init__)))
    for name, obj in inspect.getmembers(_models)
    if name.endswith('Field')
)


class ModelForm(forms.ModelForm):
    value = _models.CharField(
        choices=DJANGO_FIELD_ARGS,
        blank=False, null=False, max_length=10000)

    class Meta:
        model = models.Model


class ViewForm(forms.ModelForm):
    class Meta:
        model = models.View


class FieldValueForm(forms.ModelForm):
    ref_name = _models.CharField(
        help_text='A reference name for this key',
        max_length=500)
    blank = _models.BooleanField()
    null = _models.BooleanField()

    class Meta:
        model = models.FieldValue


class AttachModelsViewForm(forms.Form):
    pass
