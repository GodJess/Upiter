from django.contrib import admin
from main.models import Users, DebitCard, CreditCard, PlatinumCard

admin.site.register(Users)
admin.site.register(DebitCard)
admin.site.register(CreditCard)
admin.site.register(PlatinumCard)
# Register your models here.
