from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.manage_contacts, name='manage_contacts'),
    path('<int:user_id>/', views.contact_detail, name='contact_detail')
]