from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from webapp.models import Issue
from webapp.forms import IssueForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = Issue.objects.all()
        context['issues'] = issues
        return context


class IssueView(TemplateView):
    template_name = 'issue_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        context['issue'] = issue
        return context


class IssueCreateView(TemplateView):
    template_name = 'issue_Create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IssueForm()
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                descriptions=form.cleaned_data['descriptions'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('issue_view', pk=issue.pk)

        return render(request, 'issue_create.html', {'form': form})
