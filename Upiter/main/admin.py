from django.contrib import admin
from main.models import Users, DebitCard, CreditCard, PlatinumCard, Transfer, Transfers, ImageTransfers, Messenger


admin.site.register(Users)
admin.site.register(DebitCard)
admin.site.register(CreditCard)
admin.site.register(PlatinumCard)
admin.site.register(Transfer)
admin.site.register(Transfers)
admin.site.register(ImageTransfers)
admin.site.register(Messenger)
# Register your models here.
