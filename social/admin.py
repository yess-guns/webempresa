from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_reandoly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exits():
            return ('key', 'name')
        else:
            return('created', 'updated')

admin.site.register(Link, LinkAdmin)