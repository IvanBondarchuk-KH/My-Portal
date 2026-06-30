from django.contrib import admin

from .models import Profile, Note, Message


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'done',
        'created_at'
    )

    list_filter = (
        'done',
    )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender',
        'recipient',
        'text',
        'created_at'
    )

    list_filter = (
        'sender',
        'recipient',
    )