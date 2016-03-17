from django.contrib import admin

# import your model
from collection.models import Thing

# setup automatic slug creation
class ThingAdmin(admin.ModelAdmin):
    model=Thing
    list_display = ('name', 'pan',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Thing, ThingAdmin)
