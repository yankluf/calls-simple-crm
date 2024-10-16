from django.urls import path
from .views import HomePageView, TaskListView, NewContactView, NewInteractionView, FormSnippetView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('new-contact/', NewContactView.as_view(), name='new-contact'),
    path('new-interaction/', NewInteractionView.as_view(), name='new-interaction'),
    path('form-snippet/', FormSnippetView.as_view(), name='form-snippet'),
]