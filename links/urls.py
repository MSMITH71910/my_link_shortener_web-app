from django.urls import path
from .views import index, edit_link, delete_link

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('add/', index, name='add_link'),  # Add link
    path('edit/<slug:slug>/', edit_link, name='edit_link'),  # Edit link
    path('delete/<slug:slug>/', delete_link, name='delete_link'),  # Delete link
]