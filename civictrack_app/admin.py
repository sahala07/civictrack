from django.contrib import admin
from .models import Issue, ContactMessage


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'user',
        'category',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'category'
    )

    search_fields = (
        'title',
        'description',
        'location',
        'user__username'
    )

    fields = (
        'user',
        'title',
        'category',
        'description',
        'location',
        'image',
        'status',
        'resolution_note',
        'resolution_image'
    )

      # 🔥 THIS MAKES STATUS EDITABLE FROM LIST PAGE
    list_editable = (
        'status',
    )

    # 🔥 CLICK ROW TO EDIT FULL FORM
    list_display_links = (
        'id',
        'title',
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'created_at'
    )