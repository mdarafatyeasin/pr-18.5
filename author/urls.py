from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('sign_up/', views.userRegistration, name='sign_up'),
    # path('login/', views.user_login, name='log_in'),
    path('login/', views.login_views.as_view(), name='log_in'),
    path('logout/', views.log_out, name='logout'),
    # path('logout/', views.logout_view.as_view(), name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/pass_change', views.pass_change, name='pass_change'),
]