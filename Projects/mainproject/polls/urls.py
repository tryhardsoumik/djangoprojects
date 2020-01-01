

from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    # map the particular link and pass to task_id
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    # <> whenever you want to capture id from link
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),
    path('contact', views.contact, name='contact'),
    path('Aboutus', views.Aboutus, name='Aboutus'),

]