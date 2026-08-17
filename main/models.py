from django.db import models


class ContactMessage(models.Model):
    ism_familiya = models.CharField(max_length=200, default='', verbose_name="Ism va Familiya")
    telefon = models.CharField(max_length=20, default='', verbose_name="Telefon raqami")
    manzil = models.CharField(max_length=200, default='', verbose_name="Manzil (Andijon tumani)")
    xabar = models.TextField(blank=True, default='', verbose_name="Qo'shimcha xabar")
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")
    korildi = models.BooleanField(default=False, verbose_name="Ko'rildi")

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "📩 Buyurtmalar"
        ordering = ['-yaratilgan_vaqt']

    def __str__(self):
        return f"{self.ism_familiya} — {self.telefon}"


class BotJavob(models.Model):
    buyurtma = models.ForeignKey(ContactMessage, on_delete=models.CASCADE, related_name='javoblar', verbose_name="Buyurtma")
    matn = models.TextField(verbose_name="Javob matni")
    vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Javob vaqti")
    korildi = models.BooleanField(default=False, verbose_name="Mijoz ko'rdimi")

    class Meta:
        verbose_name = "Bot Javob"
        verbose_name_plural = "💬 Bot Javoblar"
        ordering = ['vaqt']

    def __str__(self):
        return f"Javob #{self.buyurtma.id} — {self.vaqt.strftime('%d.%m.%Y %H:%M')}"


class Feature(models.Model):
    icon = models.CharField(max_length=10, default='⭐', verbose_name="Emoji belgisi")
    sarlavha = models.CharField(max_length=100, default='', verbose_name="Sarlavha")
    matn = models.TextField(default='', verbose_name="Tavsif matni")
    tartib = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    faol = models.BooleanField(default=True, verbose_name="Saytda ko'rsatilsin")

    class Meta:
        verbose_name = "Afzallik"
        verbose_name_plural = "⭐ Afzalliklar"
        ordering = ['tartib']

    def __str__(self):
        return self.sarlavha


class FAQ(models.Model):
    savol = models.CharField(max_length=300, default='', verbose_name="Savol")
    javob = models.TextField(default='', verbose_name="Javob")
    tartib = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    faol = models.BooleanField(default=True, verbose_name="Saytda ko'rsatilsin")

    class Meta:
        verbose_name = "Savol-Javob"
        verbose_name_plural = "❓ Savol-Javoblar"
        ordering = ['tartib']

    def __str__(self):
        return self.savol


class Soha(models.Model):
    icon = models.CharField(max_length=10, default='🏠', verbose_name="Emoji belgisi")
    nomi = models.CharField(max_length=100, default='', verbose_name="Soha nomi (Masalan: Uylar)")
    matn = models.TextField(default='', verbose_name="Qisqacha ta'rifi")
    tartib = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    faol = models.BooleanField(default=True, verbose_name="Saytda ko'rsatilsin")

    class Meta:
        verbose_name = "Qo'llash sohasi"
        verbose_name_plural = "🏢 Qo'llash sohalari"
        ordering = ['tartib']

    def __str__(self):
        return self.nomi

