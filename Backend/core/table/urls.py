from django.urls import path
from .views import TableListView

urlpatterns = [
    path('table/', TableListView.as_view())
]
