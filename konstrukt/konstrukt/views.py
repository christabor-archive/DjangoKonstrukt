from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
import models
import forms


def home(request):
    # No optimization is done here - customize
    # for your own needs.
    all_models = models.Model.objects.all().select_related('FieldValue')
    all_views = models.View.objects.all().select_related('FieldValue')
    all_fields = models.FieldValue.objects.all()
    if request.method == 'POST':
        if 'add-field' in request.POST:
            field_form = forms.FieldValueForm(request.POST)
            if field_form.is_valid():
                field_form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Successfully added new field value')
                return HttpResponseRedirect(request.path)
        if 'add-model' in request.POST:
            model_form = forms.ModelForm(request.POST)
            if model_form.is_valid():
                model_form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Successfully added new model')
                return HttpResponseRedirect(request.path)
        if 'add-view' in request.POST:
            view_form = forms.ViewForm(request.POST)
            if view_form.is_valid():
                view_form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Successfully added new view')
                return HttpResponseRedirect(request.path)
    else:
        model_form = forms.ModelForm()
        view_form = forms.ModelForm()
        field_form = forms.FieldValueForm()
    return render(
        request, 'layouts/home.html', {
            'view_form': view_form,
            'model_form': model_form,
            'field_form': field_form,
            'all_models': all_models,
            'all_fields': all_fields,
            'all_views': all_views
        })


def view_model(request, id):
    _model = get_object_or_404(
        models.Model.objects.select_related('FieldValue'), pk=id)
    return render(request, 'layouts/model.html', {'model': _model})


def view_view(request, id):
    if request.method == 'POST':
        form = forms.AttachModelsViewForm(
            request.POST, initial={'models': models.Model.objects.all()})
        if form.is_valid():
            # TODO add logic to
            # process view
            # model data
            pass
            messages.add_message(
                request, messages.SUCCESS, 'Added models to view.')
            return HttpResponseRedirect(request.path)
    else:
        form = forms.AttachModelsViewForm(
            initial={'models': models.Model.objects.all()})
    _view = get_object_or_404(models.View, pk=id)
    return render(
        request, 'layouts/view.html', {'view': _view, 'form': form})
