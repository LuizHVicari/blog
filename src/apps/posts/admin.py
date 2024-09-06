from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ['text', 'post_type', 'created_at']
    fieldsets = (
        (None, {
            'fields': (
                'cover_image', 'description', 'text', 'title', 'category', 'post_type'
            )
        }),
    )



