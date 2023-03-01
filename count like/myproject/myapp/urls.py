from django.urls import path
from myapp.views import index, update_count

urlpatterns = [
    path('', index, name='index'),
    path('update_count/', update_count, name='update_count'),
]
