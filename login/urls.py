from django.urls import path,include
from . import views
urlpatterns=[
    path('login',views.user_login,name='user_login'),
    path('login1',views.manager_login,name='manager_login'),
    path('signup',views.user_signup,name='user_signup'),
    path('signup1',views.manager_signup,name='manager_signup'),
    path('dashboard/',include('customer.urls')),
    path('dashboard1/',include('book_manager.urls')),
    path('add-book/',include('book_manager.urls'))
]