from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, View
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
            types = form.cleaned_data.pop('types')
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                descriptions=form.cleaned_data['descriptions'],
                status=form.cleaned_data['status']
            )
            issue.types.set(types)
            return redirect('issue_view', pk=issue.pk)

        return render(request, 'issue_create.html', {'form': form})


class IssueUpdateView(View):
    def dispatch(self, request, *args, **kwargs):
        self.issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = IssueForm(initial={
            'summary': self.issue.summary,
            'descriptions': self.issue.descriptions,
            'status': self.issue.status,
            'types': self.issue.types.all()
        })
        return render(request, 'issue_update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            self.issue.summary = form.cleaned_data.get('summary')
            self.issue.descriptions = form.cleaned_data.get('descriptions')
            self.issue.status = form.cleaned_data.get('status')
            self.issue.save()
            self.issue.types.set(types)
            return redirect('issue_view', pk=self.issue.pk)
        return render(request, 'issue_update.html', {'form': form})


class IssueDeleteView(TemplateView):
    template_name = 'issue_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        context['issue'] = issue
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        issue.delete()
        return redirect('index')