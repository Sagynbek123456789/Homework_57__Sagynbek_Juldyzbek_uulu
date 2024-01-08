from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import Project
from django.shortcuts import redirect
from django.views import View
from webapp.models import Project
from django.contrib.auth.mixins import PermissionRequiredMixin


class ProjectRemoveUserView(PermissionRequiredMixin, View):
    permission_required = 'webapp.change_project'

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        user_id = request.POST.get('user_id')
        user = get_object_or_404(get_user_model(), pk=user_id)
        project.users.remove(user)
        return redirect('webapp:project_view', pk=project.pk)

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        users = project.users.all()
        return render(request, 'users/remove_user_from_project.html', {'project': project, 'users': users})
#
# class ProjectAddUserView(PermissionRequiredMixin, View):
#     permission_required = 'webapp.change_project'
#
#     def post(self, request, *args, **kwargs):
#         project = get_object_or_404(Project, pk=self.kwargs['pk'])
#         user_id = request.POST.get('user_id')
#         user = get_object_or_404(get_user_model(), pk=user_id)
#         project.users.add(user)
#         return redirect('webapp:project_view', pk=project.pk)
#
#     def get(self, request, *args, **kwargs):
#         project = get_object_or_404(Project, pk=self.kwargs['pk'])
#         users = get_user_model().objects.exclude(projects=project)
#         return render(request, 'users/add_user_to_project.html', {'project': project, 'users': users})
#
#

