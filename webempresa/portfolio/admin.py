from django.contrib import admin
from .models import Project, About
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Project, ProjectAdmin)


class AboutAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(About, AboutAdmin)