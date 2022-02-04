from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name="manager_dashboard"),
    path('new/',views.add_book,name="add_book"),
    path('update/<int:book_no>/',views.update_book,name="update_book"),

]
