from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

# from ..uzima_borehole.urls import urlpatterns

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('products/',views.products, name='products'),
    path('store/',views.store, name='store'),
    path('register/',views.register, name='register'),
    path('login/',views.login_views, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('clients/add/', views.add_client, name='add_client'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('clients/', views.client_list, name='clients'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),

    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),

    path('staff/', views.staff_list, name='staff_list'),
    path('staff/add/', views.add_staff, name='add_staff'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),

    path('drilling-requests/', views.drilling_requests, name='drilling_requests'),

    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),

    path('drilling-requests/add/', views.add_drilling_request, name='add_drilling_request'),

]