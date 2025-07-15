from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fan/<int:fan_id>/', views.ustozlar, name='ustozlar'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/fanlar/', views.fanlar_boshqaruv, name='fanlar_boshqaruv'),
    path('admin-dashboard/fanlar/delete/<int:fan_id>/', views.fan_ochirish, name='fan_ochirish'),
    path('admin-dashboard/ustozlar/', views.ustozlar_boshqaruv, name='ustozlar_boshqaruv'),
    path('admin-dashboard/ustozlar/delete/<int:ustoz_id>/', views.ustoz_ochirish, name='ustoz_ochirish'),
    path('admin-dashboard/fanlar/edit/<int:fan_id>/', views.fan_ozgartirish, name='fan_ozgartirish'),
    path('admin-dashboard/ustozlar/edit/<int:ustoz_id>/', views.ustoz_ozgartirish, name='ustoz_ozgartirish'),
    path('aloqalar/', views.aloqalar, name='aloqalar'),
    path('admin-dashboard/ustoz-qoshish/', views.ustoz_qoshish, name='ustoz_qoshish'), 
    path('admin-dashboard/ustoz-qoshish/', views.ustoz_qoshish, name='ustoz_qoshish'),
    path('aloqa-ochirish/<int:aloqa_id>/', views.aloqa_ochirish, name='aloqa_ochirish'),
]