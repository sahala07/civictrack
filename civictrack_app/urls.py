from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('guidelines/', views.guidelines, name='guidelines'),

    path('contact/', views.contact, name='contact'),

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path(
        'submit-issue/',
        views.submit_issue,
        name='submit_issue'
    ),

    path(
        'my-issues/',
        views.my_issues,
        name='my_issues'
    ),

    path(
        'issues/',
        views.issue_list,
        name='issue_list'
    ),

    path(
        'issue/<int:issue_id>/',
        views.issue_detail,
        name='issue_detail'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'authority-dashboard/',
        views.authority_dashboard,
        name='authority_dashboard'
    ),

    path(
        'update-issue/<int:issue_id>/',
        views.update_issue,
        name='update_issue'
    ),
    
    path('dashboard/', views.dashboard, name='dashboard'),
]