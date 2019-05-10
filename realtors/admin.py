from django.contrib import admin

from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','is_mvp','hire_date')
    list_display_links = ('id','name','email')
    list_editable = ('is_mvp',)
    list_filter = ('name',)
    search_fields = ('phone','description','email')
    list_per_page = 10


admin.site.register(Realtor, RealtorAdmin)
