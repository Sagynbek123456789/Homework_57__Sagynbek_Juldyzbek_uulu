from django import forms
from webapp.models import Type, Status


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=50, label='Краткое описание')
    descriptions = forms.CharField(widget=forms.Textarea, required=False, label='Полное описание')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип', widget=forms.CheckboxSelectMultiple)


