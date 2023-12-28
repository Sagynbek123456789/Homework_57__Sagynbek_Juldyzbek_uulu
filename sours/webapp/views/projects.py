from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Project
from webapp.forms import SimpleSearchForm, ProjectForm
from django.utils.http import urlencode
from django.shortcuts import reverse


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


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_view.html'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projects/project_create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


# class IndexView(TemplateView):
#     template_name = 'projects/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         issues = Issue.objects.all()
#         context['issues'] = issues
#         return context

