from django.contrib import admin

from adminpanel.models import Clients, Sites, Articles, Notifications, FilterWords

admin.site.register(Clients)
admin.site.register(Sites)
admin.site.register(FilterWords)
admin.site.register(Notifications)
admin.site.register(Articles)
