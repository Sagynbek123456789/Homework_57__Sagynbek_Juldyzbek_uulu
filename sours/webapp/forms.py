from django import forms
from webapp.models import Type, Status
from webapp.models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'descriptions', 'status', 'types']
        widgets = {
            'types': forms.CheckboxSelectMultiple()
        }



# class IssueForm(forms.ModelForm):
#     summary = forms.CharField(max_length=50, label='Краткое описание')
#     descriptions = forms.CharField(widget=forms.Textarea, required=False, label='Полное описание')
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')
#     types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип', widget=forms.CheckboxSelectMultiple)
