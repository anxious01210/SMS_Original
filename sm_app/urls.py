from django.urls import path

from sm_app import views, HoDViews

app_name = 'sm_app'

urlpatterns = [
    path('demo/', views.ShowDemoPage, name='showdemopage'),
    path('', views.ShowLoginPage, name='showloginpage'),
    path('dologin/', views.DoLogin, name='dologin'),
    path('get_user_details/', views.GetUserDetails, name='getuserdetails'),
    path('logout_user/', views.LogoutUser, name='logoutuser'),
    path('admin_home/', HoDViews.admin_home, name='admin_home'),
    path('add_teacher/', HoDViews.add_teacher, name='add_teacher'),
    path('add_staff_save/', HoDViews.add_staff_save, name='add_staff_save'),

]
