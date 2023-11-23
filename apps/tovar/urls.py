from django.urls import path
from .views import TovarListView


urlpatterns = [
    path('tova-list', TovarListView.as_view(), name='Tovar-List')
]

