from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, View
from webapp.models import Issue
from webapp.forms import IssueForm


# Create your views here.

class IssueView(TemplateView):
    template_name = 'issues/issue_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        context['issue'] = issue
        return context


class IssueCreateView(TemplateView):
    template_name = 'issues/issue_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IssueForm()
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = form.save()
            return redirect('issue_view', pk=issue.pk)

        return render(request, 'issues/issue_create.html', {'form': form})


class IssueUpdateView(View):
    def dispatch(self, request, *args, **kwargs):
        self.issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = IssueForm(instance=self.issue)
        return render(request, 'issues/issue_update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(instance=self.issue, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('issue_view', pk=self.issue.pk)
        return render(request, 'issues/issue_update.html', {'form': form})


class IssueDeleteView(TemplateView):
    template_name = 'issues/issue_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        context['issue'] = issue
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        issue.delete()
        return redirect('index')


