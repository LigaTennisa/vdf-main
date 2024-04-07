
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('post/create', views.create_post, name='post-create'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>/', views.delete_post, name='post-delete'),
    path('about/', views.about, name='about'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('courts/', views.courts, name='courts'),
    path('training/', views.training, name='training'),
    path('pravila/', views.pravila, name='pravila'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('find_partner/', views.find_partner, name='find_partner'),
    path('add_post/', views.add_post, name='add_post'),
    path('find-partner/', views.find_partner, name='find-partner'),
    path('respond_to_post/<int:id>/',
         views.respond_to_post, name='respond_to_post'),
    path('accept_responder/<int:post_id>/',
         views.accept_responder, name='accept_responder'),
    path('cancel_responder/<int:post_id>/',
         views.cancel_responder, name='cancel_responder'),
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('responders_list/<int:post_id>/',
         views.responders_list, name='responders_list')
]
