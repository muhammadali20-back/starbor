from django.contrib import admin
from .models import ContactMessage, Feature, FAQ, BotJavob, Soha


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['ism_familiya', 'telefon', 'manzil', 'yaratilgan_vaqt', 'korildi']
    list_filter = ['korildi', 'yaratilgan_vaqt']
    search_fields = ['ism_familiya', 'telefon', 'manzil']
    list_editable = ['korildi']
    readonly_fields = ['yaratilgan_vaqt']
    ordering = ['-yaratilgan_vaqt']
    list_per_page = 20

    fieldsets = (
        ("Mijoz ma'lumotlari", {
            'fields': ('ism_familiya', 'telefon', 'manzil', 'xabar')
        }),
        ("Holat", {
            'fields': ('korildi', 'yaratilgan_vaqt')
        }),
    )

class BotJavobInline(admin.TabularInline):
    model = BotJavob
    extra = 0
    readonly_fields = ['vaqt']

ContactMessageAdmin.inlines = [BotJavobInline]


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['icon', 'sarlavha', 'tartib', 'faol']
    list_editable = ['tartib', 'faol']
    list_per_page = 20


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['savol', 'tartib', 'faol']
    list_editable = ['tartib', 'faol']
    list_per_page = 20


@admin.register(Soha)
class SohaAdmin(admin.ModelAdmin):
    list_display = ['icon', 'nomi', 'tartib', 'faol']
    list_editable = ['tartib', 'faol']
    list_per_page = 20
