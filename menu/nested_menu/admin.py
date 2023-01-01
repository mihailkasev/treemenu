from django.contrib import admin

from nested_menu.models import Menu, Thing


class ThingAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    fieldsets = ((
        'Добавь новый предмет',
        {
            'description': "Выберите menu, при необходимости выберите parent",
            'fields': (('menu', 'parent'), 'title', 'slug')
        }
    ),)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


admin.site.register(Thing, ThingAdmin)
admin.site.register(Menu, MenuAdmin)
