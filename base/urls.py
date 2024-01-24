from django.urls import path
from . import views
# from .views import SignUpView, LoginView, DashboardView


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),   
     path('',views.home, name="home" ),
    path('room/<str:pk>/', views.room, name="room"),
    path('astronomy_club/',views.astronomy_club,name='astronomy_club'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('dashboard/', DashboardView.as_view(), name='dashboard'),
]

