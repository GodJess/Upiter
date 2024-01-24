from django.contrib import admin
from main.models import Users, DebitCard, CreditCard, PlatinumCard, Transfer, Transfers, ImageTransfers

admin.site.register(Users)
admin.site.register(DebitCard)
admin.site.register(CreditCard)
admin.site.register(PlatinumCard)
admin.site.register(Transfer)
admin.site.register(Transfers)
admin.site.register(ImageTransfers)
# Register your models here.
