from django.contrib import admin

# Register your models here.
from realtors.models import Realtor


# to customize admin dashboard


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_mvp',)
    search_fields = ('name', 'email')
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
