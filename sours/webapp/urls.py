from django.urls import path
from webapp.views import IssueView, IssueCreateView, IssueUpdateView, IssueDeleteView, \
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from webapp.views.users import ProjectRemoveUserView


app_name = 'webapp'


urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('issues/<int:pk>', IssueView.as_view(), name='issue_view'),
    path('issues/<int:pk>/add/', IssueCreateView.as_view(), name='issue_add_view'),
    path('issues/<int:pk>/edit/', IssueUpdateView.as_view(), name='issue_update_view'),
    path('issues/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete_view'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_view'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_add_view'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update_view'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete_view'),
    path('projects/<int:pk>/remove_user/<int:user_id>/', ProjectRemoveUserView.as_view(), name='remove_user_from_project')
    # path('projects/<int:pk>/add-user/', ProjectAddUserView.as_view(), name='add_user_to_project')

]