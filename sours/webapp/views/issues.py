from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import TemplateView, View, CreateView, UpdateView, DetailView, DeleteView
from webapp.models import Issue, Project
from webapp.forms import IssueForm


# Create your views here.

class IssueView(View):
    template_name = 'issues/issue_view.html'
    model = Issue


class IssueCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'issues/issue_create.html'
    form_class = IssueForm
    permission_required = 'webapp.change_issue'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        form.save_m2m()
        return redirect('webapp:project_view', pk=project.pk)

    def has_permission(self):
        return self.request.user.has_perm('webapp.delete_project') or self.request.user == self.get_object().summary


class IssueUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'issues/issue_update.html'
    model = Issue
    form_class = IssueForm
    permission_required = 'webapp.change_issue'

    def has_permission(self):
        return self.request.user.has_perm('webapp.delete_project') or self.request.user == self.get_object().summary

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.project.pk})


class IssueDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'issues/issue_delete.html'
    model = Issue
    permission_required = 'webapp.change_issue'

    def has_permission(self):
        return self.request.user.has_perm('webapp.delete_project') or self.request.user == self.get_object().summary

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.project.pk})



