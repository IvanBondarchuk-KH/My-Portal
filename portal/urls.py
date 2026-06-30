from django.urls import path

from . import views


urlpatterns = [

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'dashboard/',
        views.dashboard_view,
        name='dashboard'
    ),

    path(
        'profile/',
        views.profile_view,
        name='profile'
    ),

    path(
        'notes/',
        views.notes_view,
        name='notes'
    ),

    path(
        'note/<int:note_id>/toggle/',
        views.toggle_note,
        name='toggle_note'
    ),

    path(
        'note/<int:note_id>/delete/',
        views.delete_note,
        name='delete_note'
    ),

    path(
        'messages/', 
        views.inbox, 
        name='inbox'
    ),

    path(
        'messages/users/', 
        views.user_list, 
        name='user_list'
    ),

    path(
        'messages/<int:user_id>/', 
        views.chat, 
        name='chat'
    ),
]