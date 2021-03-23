from django.contrib import admin

from .models import Country, Language, Education, ActionArea, TalkThemes
# Register your models here.
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(ActionArea)
admin.site.register(TalkThemes)
