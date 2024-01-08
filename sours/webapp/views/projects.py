from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Project
from webapp.forms import SimpleSearchForm, ProjectForm
from django.utils.http import urlencode
from django.shortcuts import reverse, redirect, get_object_or_404, render
from django.urls import reverse_lazy


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) |
                                       Q(descriptions__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_view.html'
    permission_required = 'webapp.view_project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        users = project.users.all()
        context['users'] = users
        return context


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_create.html'
    form_class = ProjectForm
    permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.title = self.request.user
        self.object.save()
        # form.save_m2m()
        return redirect(self.get_success_url())


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.has_perm('webapp.delete_project') or self.request.user == self.get_object().author


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('webapp:index')
    # permission_required = 'webapp.delete_project'

    def has_permission(self):
        return self.request.user.has_perm('webapp.delete_project')

#
# class ProjectAddUserView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
#     model = Project
#     template_name = 'users/add_user_to_project.html'
#     permission_required = 'webapp.change_project'
#
#     def post(self, request, *args, **kwargs):
#         project = self.get_object()
#         user_id = request.POST.get('user_id')
#         user = get_object_or_404(get_user_model(), pk=user_id)
#         project.users.add(user)
#         return redirect('webapp:project_view', pk=project.pk)
#
#     def add_user_to_project(request, project_id):
#         project = get_object_or_404(Project, pk=project_id)
#         users = get_user_model().objects.exclude(projects=project)
#         if request.method == 'POST':
#             user_id = request.POST.get('user_id')
#             user = get_object_or_404(get_user_model(), pk=user_id)
#             project.users.add(user)
#             return redirect('webapp:project_view', pk=project_id)
#         return render(request, 'users/add_user_to_project.html',
#                       {'project': project, 'users': users})
#
#
# class ProjectRemoveUserView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
#     model = Project
#     template_name = 'users/remove_user_from_project.html'
#     permission_required = 'webapp.change_project'
#
#     def post(self, request, *args, **kwargs):
#         project = self.get_object()
#         user_id = request.POST.get('user_id')
#         user = get_object_or_404(get_user_model(), pk=user_id)
#         project.users.remove(user)
#         return redirect('webapp:project_view', pk=project.pk)
#
#
# class UsersListView(View):
#         template_name = 'users/users_list.html'
#         model = Project
#
#     def project_users_list(request, project_id):
#         project = get_object_or_404(Project, pk=project_id)
#         users = project.projectuser_set.all()
#         return render(request, 'users/users_list.html', {'project': project, 'users': users})