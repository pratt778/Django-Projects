from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee,name='employee'),
    path('add',views.add,name='add'),
    path('edit/<eid>',views.edit,name='edit'),
    path('del/<eid>',views.delete,name='delete')
]
