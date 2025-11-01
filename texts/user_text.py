from deep_translator import GoogleTranslator

GENDER_TEXT = """
🛍️ Kim uchun kiyim xarid qilmoqchisiz?

Iltimos, quyidagilardan birini tanlang:
👕 Erkaklar uchun
👗 Ayollar uchun
🧒 Bolalar uchun

Har bir bo‘limda siz uchun moda, sifat va 
qulay narx uyg‘unligini topasiz ✨"""


CATEGORY_TEXT = """
😊 Zo‘r!
Endi qaysi turdagi kiyimni ko‘rmoqchisiz?
Quyidagi ro‘yxatdan tanlang 👇"""

SEASON_TEXT = """🌤️ Endi mavsumni tanlang

Qaysi fasl uchun kiyim izlayapsiz?
👇 Quyidagi variantlardan birini tanlang:"""


def menu_oxiri(gender,category,season):
    jins = GoogleTranslator(source= "auto", target="uz").translate(gender)
    turi = GoogleTranslator(source= "auto", target="uz").translate(category)
    fasl = GoogleTranslator(source= "auto", target="uz").translate(season)
    r = ""
    for i in range(len(turi)):
        if i == 2:
            r+=turi[i].upper()
        else:
            r+=turi[i]
    return f"""🛍️ Sizning tanlovingiz:
👤 Jins: {jins.capitalize()}
👕 Kategoriya: {r}
🌦️ Mavsum: {fasl.capitalize()}

Endi siz uchun mos kiyimlarni ko‘rsatamiz 👇"""