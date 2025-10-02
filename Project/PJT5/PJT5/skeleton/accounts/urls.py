from django.urls import path
from . import views
# from django.views.generic.base import RedirectView

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('stock_delete/<int:pk>/', views.stock_delete, name='stock_delete'),
]
