import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starbor_web.settings')
django.setup()

from main.models import Feature, FAQ

def run():
    # Clear existing
    Feature.objects.all().delete()
    FAQ.objects.all().delete()

    # Create Features
    features = [
        {"icon": "🇹🇷", "sarlavha": "Haqiqiy Turk Sifati", "matn": "Barcha xomashyo va uskunalar Turkiyadan keltirilgan. Bu jahon standartiga to'la javob beradigan sifat degani.", "tartib": 1},
        {"icon": "🛡️", "sarlavha": "100% Choksiz Himoya", "matn": "Sepilganda barcha teshik va yoriqlarni to'ldiradi. Havo va namlik o'tadigan hech qanday chok (shov) qolmaydi.", "tartib": 2},
        {"icon": "💰", "sarlavha": "Energiyani Tejash", "matn": "Isitish va sovitish xarajatlarini 50-60% gacha tejaydi. Tez orada sarflagan pulingizni oqlaydi.", "tartib": 3},
        {"icon": "🔇", "sarlavha": "Ovoz O'tkazmaslik", "matn": "Faqat issiqlik emas, balki ko'chadagi shovqinlarni ham to'sib, uyingizda tinchlik va osoyishtalikni ta'minlaydi.", "tartib": 4},
    ]

    for f in features:
        Feature.objects.create(**f)

    # Create FAQs
    faqs = [
        {"savol": "Qancha vaqt xizmat qiladi?", "javob": "To'g'ri o'rnatilgan STARBOR poliuretan izolyatsiyasi o'z xususiyatlarini kamida 20-25 yil davomida saqlab qoladi. U chirimaydi va o'tirmaydi.", "tartib": 1},
        {"savol": "Kemiruvchilar (sichqon) yemaydimi?", "javob": "Yo'q! Bu material kemiruvchilar va hasharotlar uchun mutlaqo ozuqa hisoblanmaydi, shuning uchun ular unga tegmaydi.", "tartib": 2},
        {"savol": "Qishda qanday, yozda qanday?", "javob": "Bu izolyatsiya termal to'siq bo'lib xizmat qiladi. Qishda uydagi issiqlikni tashqariga chiqarmaydi, yozda esa tashqaridagi jazirama issiqni uy ichiga kiritmaydi.", "tartib": 3},
        {"savol": "Andijondan tashqariga ham borasizlarmi?", "javob": "Hozirgi kunda asosiy va sifatli xizmat ko'rsatish hududimiz asosan Andijon viloyati va uning tumanlari hisoblanadi.", "tartib": 4},
    ]

    for faq in faqs:
        FAQ.objects.create(**faq)

    print("Bazaga barcha ma'lumotlar muvaffaqiyatli qo'shildi!")

if __name__ == '__main__':
    run()
