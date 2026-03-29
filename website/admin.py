from django.contrib import admin
from website.models import Contact, newslatters

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_data'
    list_display = ('id', 'name', 'email', 'created_data')
    list_filter = ('email',)
    search_fields = ('name', 'massage')
class NewslattersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register(newslatters, NewslattersAdmin)

