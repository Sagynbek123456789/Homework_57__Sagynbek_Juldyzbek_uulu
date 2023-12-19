from django.shortcuts import render
from django.views.generic import TemplateView
from webapp.models import Issue


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = Issue.objects.all()
        context['issues'] = issues
        return context
