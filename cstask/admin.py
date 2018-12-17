from django.contrib import admin
from . models import Topic,Entry
# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ['name','created_at','owner']
    search_fields = ('name',)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Entry)
