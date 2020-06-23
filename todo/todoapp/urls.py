from django.urls import path
from . import views


urlpatterns = [
   path('',views.home),
   path('create/',views.create,name='create'),
   path('delete/<goals_id>',views.delete_post,name='delete'),




]
