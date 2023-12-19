from django.urls import path
from webapp.views import IndexView, IssueView, IssueCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issues/<int:pk>', IssueView.as_view(), name='issue_view'),
    path('issues/add/', IssueCreateView.as_view(), name='issue_add_view')
]