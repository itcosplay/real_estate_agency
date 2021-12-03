from django.contrib import admin

from .models import Flat
from .models import Claim

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town','address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text']
    raw_id_fields = ['user']