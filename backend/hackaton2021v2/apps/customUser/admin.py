from django.contrib import admin
from .models import Role, Skill, Portfolio, improvedUserModel

admin.site.register(Role)
admin.site.register(Skill)
admin.site.register(Portfolio)
admin.site.register(improvedUserModel)