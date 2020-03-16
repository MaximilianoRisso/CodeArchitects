
from django.contrib import admin
from .models import Profile, Product

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(PendingOrder)
admin.site.register(ProcessedOrder)