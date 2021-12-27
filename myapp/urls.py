from django.urls import path
from . import views


urlpatterns = [
    path('',views.add),
    path('add/',views.add,name="add_list"),
    path('update/<int:id>',views.update,name="update_list"),
    path('delete/<int:id>',views.delete,name="delete_list"),
]
