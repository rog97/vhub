from django.contrib import admin

# Register your models here.

from .models import Startup

class StartupAdmin(admin.ModelAdmin):
    list_display = ["__str__", "latest_funding", "description"]
    search_fields = ["name","description"]
    list_filter = ["latest_funding"]
    list_editable = ["description"]
    class Meta:
        model = Startup

admin.site.register(Startup, StartupAdmin)
