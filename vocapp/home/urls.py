from django.urls import path
from .import views

urlpatterns = [
# ---- homepage -----
    path('', views.index_page, name='index'),
    path('contact', views.contact_page,name='contact'),

    path('register', views.register_page, name='register_page'),
    path('register/ok', views.register_ok_page, name ='register_ok_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.login_page, name='logout_page'),

# ---- dashboard -----

    path('dashboard', views.dashboard_page, name='dashboard_page'),
    path('voc_add', views.voc_add, name='voc_add'),

]
