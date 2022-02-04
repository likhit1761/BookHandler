from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('book',views.book,name='book'),
    path('contact-us',views.contact,name='contact-us'),
    path('book-now/<str:id>',views.book_now,name='book-now'),
    path('cancel-book/<str:id>',views.cancel_book,name='cancel-book'),
    path('delete-book/<str:id>',views.delete_book,name='delete-book'),
    path('confirm-now-booking',views.book_confirm,name="book_confirm")

]