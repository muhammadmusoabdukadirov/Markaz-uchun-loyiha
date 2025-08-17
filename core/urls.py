from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home, user_logout,
    ustoz_ochirish, ustoz_ozgartirish, ustoz_qoshish,
    ustozlar, ustozlar_boshqaruv,
    admin_dashboard,
    aloqa_ochirish, aloqalar,
    fan_ochirish, fan_ozgartirish,
    fanlar_boshqaruv, fanlar_list
)

urlpatterns = [
    path('', home, name='home'),  # Bosh sahifa
    path('fanlar/', fanlar_list, name='all_fans'),  # Barcha fanlar sahifasi
    path('fan/<int:fan_id>/', ustozlar, name='ustozlar'),  # Har bir fan uchun ustozlar
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    
    # Fanlar boshqaruv
    path('admin-dashboard/fanlar/', fanlar_boshqaruv, name='fanlar_boshqaruv'),
    path('admin-dashboard/fanlar/delete/<int:fan_id>/', fan_ochirish, name='fan_ochirish'),
    path('admin-dashboard/fanlar/edit/<int:fan_id>/', fan_ozgartirish, name='fan_ozgartirish'),
    
    # Ustozlar boshqaruv
    path('admin-dashboard/ustozlar/', ustozlar_boshqaruv, name='ustozlar_boshqaruv'),
    path('admin-dashboard/ustozlar/delete/<int:ustoz_id>/', ustoz_ochirish, name='ustoz_ochirish'),
    path('admin-dashboard/ustozlar/edit/<int:ustoz_id>/', ustoz_ozgartirish, name='ustoz_ozgartirish'),
    path('admin-dashboard/ustoz-qoshish/', ustoz_qoshish, name='ustoz_qoshish'),

    # Aloqalar
    path('aloqalar/', aloqalar, name='aloqalar'),
    path('aloqa-ochirish/<int:aloqa_id>/', aloqa_ochirish, name='aloqa_ochirish'),

    # Logout
    path('logout/', user_logout, name='logout'),
]
