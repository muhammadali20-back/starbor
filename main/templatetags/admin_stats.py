from django import template
from django.utils import timezone
from main.models import ContactMessage
from django.db.models import Count
from django.db.models.functions import TruncMonth
import datetime

register = template.Library()

@register.simple_tag
def get_dashboard_stats():
    now = timezone.now()
    bugun_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    oy_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    jami = ContactMessage.objects.count()
    bugun = ContactMessage.objects.filter(yaratilgan_vaqt__gte=bugun_start).count()
    shu_oy = ContactMessage.objects.filter(yaratilgan_vaqt__gte=oy_start).count()

    # Oylar bo'yicha statistika (oxirgi 6 oy)
    olti_oy_oldin = now - datetime.timedelta(days=180)
    oylik_stats = (
        ContactMessage.objects.filter(yaratilgan_vaqt__gte=olti_oy_oldin)
        .annotate(month=TruncMonth('yaratilgan_vaqt'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    oy_nomlari = []
    buyurtmalar_soni = []
    
    for stat in oylik_stats:
        oy_nomlari.append(stat['month'].strftime('%B %Y'))
        buyurtmalar_soni.append(stat['count'])

    # Tumanlar kesimida statistika
    tumanlar_stats = ContactMessage.objects.values('manzil').annotate(count=Count('id')).order_by('-count')[:6]
    tuman_nomlari = [t['manzil'] for t in tumanlar_stats]
    tuman_soni = [t['count'] for t in tumanlar_stats]

    # Javob berilgan vs Kutilayotgan
    javob_berilgan = ContactMessage.objects.filter(javoblar__isnull=False).distinct().count()
    kutilayotgan = jami - javob_berilgan

    return {
        'jami': jami,
        'bugun': bugun,
        'shu_oy': shu_oy,
        'oy_nomlari': oy_nomlari,
        'buyurtmalar_soni': buyurtmalar_soni,
        'tuman_nomlari': tuman_nomlari,
        'tuman_soni': tuman_soni,
        'javob_berilgan': javob_berilgan,
        'kutilayotgan': kutilayotgan,
    }
