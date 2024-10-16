from django.contrib import admin
from .models import Contact, Interaction, Event, Task, LineOfBusiness

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email', 'tag', 'created_at')
    ordering = ('last_name',)
    search_fields = ('last_name', 'first_name', 'phone', 'email', 'tag', 'created_at')

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('contact', 'type', 'date')
    ordering = ('-date',)
    search_fields = ('contact', 'type', 'date', 'description')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('origin', 'type', 'date', 'time')
    ordering = ('-date',)
    search_fields = ('origin', 'type', 'date', 'time')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'origin', 'deadline', 'time_sensitive')
    ordering = ('-deadline',)
    search_fields = ('name', 'type', 'origin', 'deadline', 'description')

@admin.register(LineOfBusiness)
class LineOfBusinessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)