from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableInlineModelAdmin

from .models import PersonalInfo, Ability


@admin.register(PersonalInfo)
class PersonalInfoAdmin(TranslatableAdmin):
    list_display = ['name', 'created_at']
    fieldsets = (
        (None, {
            "fields": (
                'name', 'about_me', 'personal_life', 'abilities'
            ),
        }),
    )

@admin.register(Ability)
class AbilityAdmin(TranslatableAdmin):
    list_display = ['key_name', 'level', 'created_at']
    fieldsets = (
        (None, {
            "fields": (
                'key_name', 'name', 'level', 'type', 'weight'
            )
        }),
    )




