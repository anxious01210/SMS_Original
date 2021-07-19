from django.urls import path

from sm_app import views

app_name = 'sm_app'

urlpatterns = [
    path('demo/', views.ShowDemoPage, name='showdemopage'),
    path('', views.ShowLoginPage, name='showloginpage'),
    path('dologin/', views.DoLogin, name='dologin'),
    path('get_user_details/', views.GetUserDetails, name='getuserdetails'),
    path('logout_user/', views.LogoutUser, name='logoutuser'),

]
