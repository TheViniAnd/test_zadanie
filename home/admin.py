from django.contrib import admin
from .models import Mod

class DateAdmin(admin.ModelAdmin):
    model = Mod
    fields = ('title', )
    list_display = ['date_added','title',]

admin.site.register(Mod, DateAdmin)