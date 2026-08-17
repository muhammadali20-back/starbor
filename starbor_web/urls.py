from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('starbor-boss/', admin.site.urls),  # Maxfiy qilingan admin manzil
    path('', include('main.urls')),
]
