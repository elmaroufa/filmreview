from django.urls import path
from . import views

urlpatterns = [        
    path('<int:film_id>', views.detail, name='detail'),
    path('<int:film_id>/create', views.createreview, name='createreview')
]