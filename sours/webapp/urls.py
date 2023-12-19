from django.urls import path
from webapp.views import IndexView, IssueView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issues/<int:pk>', IssueView.as_view(), name='issue_view'),
]