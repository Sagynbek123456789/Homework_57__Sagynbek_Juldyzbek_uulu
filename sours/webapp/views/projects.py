from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    paginate_by = 5


# class IndexView(TemplateView):
#     template_name = 'projects/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         issues = Issue.objects.all()
#         context['issues'] = issues
#         return context

