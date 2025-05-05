from django.contrib import admin

from vaccines.models import User, Vaccine

# Register your models here.
admin.site.register(User)
admin.site.register(Vaccine)
