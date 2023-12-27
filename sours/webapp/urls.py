from django.urls import path
from webapp.views.issues import IndexView, IssueView, IssueCreateView, IssueUpdateView, IssueDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issues/<int:pk>', IssueView.as_view(), name='issue_view'),
    path('issues/add/', IssueCreateView.as_view(), name='issue_add_view'),
    path('issues/<int:pk>/edit/', IssueUpdateView.as_view(), name='issue_update_view'),
    path('issues/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete_view')
]