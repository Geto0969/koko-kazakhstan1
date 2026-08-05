from django.core.management.base import BaseCommand

from shop.models import Category, FAQ, Product, Review, SiteSettings


class Command(BaseCommand):
    help = 'Загружает демонстрационные данные для KOKO Kazakhstan'

    def handle(self, *args, **options):
        SiteSettings.objects.get_or_create(
            pk=1,
            defaults={
                'whatsapp_number': '77001234567',
                'instagram_url': 'https://www.instagram.com/koko.kazakhstan/',
                'address': 'г. Алматы, пр. Абая, 150/230',
                'working_hours': 'Пн–Сб: 10:00–20:00, Вс: 11:00–18:00',
            },
        )

        categories_data = [
            ('Очищение', 'ochishchenie', 1),
            ('Сыворотки', 'syvorotki', 2),
            ('Кремы', 'kremy', 3),
            ('SPF', 'spf', 4),
            ('Тонеры', 'tonery', 5),
            ('Маски', 'maski', 6),
        ]

        categories = {}
        for name, slug, order in categories_data:
            cat, _ = Category.objects.update_or_create(
                slug=slug,
                defaults={'name': name, 'order': order},
            )
            categories[slug] = cat

        products_data = [
            {
                'name': 'COSRX Low pH Good Morning Gel Cleanser',
                'slug': 'cosrx-low-ph-cleanser',
                'category': 'ochishchenie',
                'price': 8500,
                'short_description': 'Мягкий гель для утреннего очищения с низким pH',
                'description': 'Нежный гель-крем для ежедневного очищения кожи. '
                'Сохраняет естественный баланс pH, не пересушивает и идеально '
                'подходит для чувствительной кожи.',
                'characteristics': 'Объём: 150 мл\nТип кожи: все типы\npH: 5.5\nСтрана: Южная Корея',
                'usage': 'Нанесите небольшое количество на влажную кожу, '
                'массируйте 1–2 минуты и смойте тёплой водой.',
                'image': 'https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=800&q=80',
                'is_featured': True,
            },
            {
                'name': 'Anua Heartleaf Pore Control Cleansing Oil',
                'slug': 'anua-heartleaf-cleansing-oil',
                'category': 'ochishchenie',
                'price': 9200,
                'short_description': 'Гидрофильное масло для глубокого очищения пор',
                'description': 'Гидрофильное масло с экстрактом сердцевины листьев '
                'для бережного удаления макияжа и загрязнений из пор.',
                'characteristics': 'Объём: 200 мл\nТип кожи: жирная, комбинированная\nСтрана: Южная Корея',
                'usage': 'Нанесите на сухую кожу, массируйте и смойте водой.',
                'image': 'https://images.unsplash.com/photo-1620916560428-4d6775f65858?w=800&q=80',
                'is_featured': True,
            },
            {
                'name': 'Beauty of Joseon Glow Serum',
                'slug': 'beauty-of-joseon-glow-serum',
                'category': 'syvorotki',
                'price': 11500,
                'short_description': 'Сыворотка для сияния с пропolis и niacinamide',
                'description': 'Лёгкая сыворотка на основе прополиса и ниацинамида '
                'для ровного тона, сияния и увлажнения кожи.',
                'characteristics': 'Объём: 30 мл\nАктивы: Propolis, Niacinamide\nСтрана: Южная Корея',
                'usage': 'Нанесите 2–3 капли на очищенную кожу утром и вечером.',
                'image': 'https://images.unsplash.com/photo-1617897903246-3f0d4a0a4c5e?w=800&q=80',
                'is_featured': True,
            },
            {
                'name': 'Torriden Dive-In Low Molecule Hyaluronic Acid Serum',
                'slug': 'torriden-hyaluronic-serum',
                'category': 'syvorotki',
                'price': 10800,
                'short_description': 'Увлажняющая сыворотка с 5 видами гиалуроновой кислоты',
                'description': 'Интенсивное увлажнение с низкомолекулярной гиалуроновой '
                'кислотой для глубокого проникновения в кожу.',
                'characteristics': 'Объём: 50 мл\nТип кожи: все типы\nСтрана: Южная Корея',
                'usage': 'Нанесите после тонера, до крема.',
                'image': 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=800&q=80',
                'is_featured': True,
            },
            {
                'name': 'Dr. Jart+ Ceramidin Cream',
                'slug': 'dr-jart-ceramidin-cream',
                'category': 'kremy',
                'price': 18900,
                'short_description': 'Питательный крем с церамидами для восстановления барьера',
                'description': 'Богатый крем с 5 видами церамидов для восстановления '
                'защитного барьера и интенсивного увлажнения.',
                'characteristics': 'Объём: 50 мл\nТип кожи: сухая, чувствительная\nСтрана: Южная Корея',
                'usage': 'Нанесите на финальном этапе ухода утром и вечером.',
                'image': 'https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=800&q=80',
                'is_featured': True,
            },
            {
                'name': 'Laneige Water Bank Blue Hyaluronic Cream',
                'slug': 'laneige-water-bank-cream',
                'category': 'kremy',
                'price': 16500,
                'short_description': 'Увлажняющий крем с синей гиалуроновой кислотой',
                'description': 'Лёгкий, но насыщенный крем для длительного увлажнения '
                'и свежести кожи на протяжении всего дня.',
                'characteristics': 'Объём: 50 мл\nТип кожи: нормальная, комбинированная\nСтрана: Южная Корея',
                'usage': 'Нанесите после сыворотки.',
                'image': 'https://images.unsplash.com/photo-1596755389378-c31d7bd763f8?w=800&q=80',
                'is_featured': False,
            },
            {
                'name': 'Beauty of Joseon Relief Sun SPF50+ PA++++',
                'slug': 'beauty-of-joseon-relief-sun',
                'category': 'spf',
                'price': 9800,
                'short_description': 'Лёгкий солнцезащитный крем без белого налёта',
                'description': 'SPF50+ PA++++ с рисовыми пробиотиками. '
                'Лёгкая текстура, не оставляет липкости и белого налёта.',
                'characteristics': 'Объём: 50 мл\nSPF: 50+ PA++++\nСтрана: Южная Корея',
                'usage': 'Наносите каждое утро как последний этап ухода.',
                'image': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=800&q=80',
                'is_featured': True,
            },
            {
                'name': 'Round Lab Birch Juice Moisturizing Sun Cream SPF50+',
                'slug': 'round-lab-birch-sun-cream',
                'category': 'spf',
                'price': 10200,
                'short_description': 'Увлажняющий SPF с соком берёзы',
                'description': 'Солнцезащитный крем с увлажняющим эффектом на основе '
                'сока берёзы для комфортного ежедневного использования.',
                'characteristics': 'Объём: 50 мл\nSPF: 50+ PA++++\nСтрана: Южная Корея',
                'usage': 'Наносите за 15 минут до выхода на солнце.',
                'image': 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=800&q=80',
                'is_featured': False,
            },
            {
                'name': 'Anua Heartleaf 77% Soothing Toner',
                'slug': 'anua-heartleaf-toner',
                'category': 'tonery',
                'price': 8900,
                'short_description': 'Успокаивающий тонер с 77% экстрактом сердцевины листьев',
                'description': 'Тонер для успокоения раздражённой кожи, '
                'сужения пор и восстановления баланса.',
                'characteristics': 'Объём: 250 мл\nТип кожи: чувствительная, проблемная\nСтрана: Южная Корея',
                'usage': 'Нанесите на ватный диск или ладони, распределите по лицу.',
                'image': 'https://images.unsplash.com/photo-1612817288484-6f916006741a?w=800&q=80',
                'is_featured': True,
            },
            {
                'name': 'COSRX AHA/BHA Clarifying Treatment Toner',
                'slug': 'cosrx-aha-bha-toner',
                'category': 'tonery',
                'price': 7800,
                'short_description': 'Тонер с AHA/BHA для обновления и сияния кожи',
                'description': 'Ежедневный тонер с кислотами для мягкого отшелушивания '
                'и улучшения текстуры кожи.',
                'characteristics': 'Объём: 150 мл\nАктивы: AHA, BHA\nСтрана: Южная Корея',
                'usage': 'Используйте вечером после очищения.',
                'image': 'https://images.unsplash.com/photo-1598440947619-2c35fc3aa908?w=800&q=80',
                'is_featured': False,
            },
            {
                'name': 'Mediheal N.M.F Aquaring Ampoule Mask',
                'slug': 'mediheal-nmf-mask',
                'category': 'maski',
                'price': 1200,
                'short_description': 'Увлажняющая тканевая маска N.M.F',
                'description': 'Культовая тканевая маска с N.M.F комплексом '
                'для мгновенного увлажнения и сияния.',
                'characteristics': 'Количество: 1 шт\nТип: тканевая маска\nСтрана: Южная Корея',
                'usage': 'Нанесите на 15–20 минут, затем распределите остаток эссенции.',
                'image': 'https://images.unsplash.com/photo-1571781926291-c477eb30ae66?w=800&q=80',
                'is_featured': True,
            },
            {
                'name': 'Biodance Bio-Collagen Real Deep Mask',
                'slug': 'biodance-collagen-mask',
                'category': 'maski',
                'price': 3500,
                'short_description': 'Гидrogel-маска с коллагеном для упругости кожи',
                'description': 'Инновационная гидrogel-маска с коллагеном '
                'для глубокого увлажнения и эффекта «стеклянной кожи».',
                'characteristics': 'Количество: 1 шт\nТип: гидrogel\nСтрана: Южная Корея',
                'usage': 'Нанесите на 3–4 часа или на ночь.',
                'image': 'https://images.unsplash.com/photo-1515377900543-c722ed8d763e?w=800&q=80',
                'is_featured': False,
            },
        ]

        for data in products_data:
            category = categories[data.pop('category')]
            Product.objects.update_or_create(
                slug=data['slug'],
                defaults={**data, 'category': category},
            )

        reviews_data = [
            ('Айгуль К.', 'Заказываю уже третий раз! Косметика оригинальная, доставка быстрая. COSRX — мой фаворит.', 5),
            ('Динара М.', 'Консультант помогла подобрать уход для чувствительной кожи. Результат виден уже через неделю!', 5),
            ('Алина С.', 'Beauty of Joseon SPF — лучший солнцезащитный крем, который я пробовала. Без белого налёта!', 5),
            ('Мадина Т.', 'Очень красивая упаковка и приятные цены. Доставили в Астану за 2 дня.', 5),
            ('Жанар Б.', 'Anua тонер полностью успокоил мою кожу. Спасибо KOKO за профессиональный подход!', 5),
            ('Камила Р.', 'Biodance маска — это магия! Кожа сияет как после салона. Рекомендую всем!', 5),
        ]

        Review.objects.all().delete()
        for i, (name, text, rating) in enumerate(reviews_data):
            Review.objects.create(
                author_name=name,
                text=text,
                rating=rating,
                order=i,
            )

        faqs_data = [
            (
                'Как оформить заказ?',
                'Выберите товар в каталоге и нажмите «Заказать через WhatsApp». '
                'Мы ответим в течение 15 минут и поможем оформить доставку.',
            ),
            (
                'Доставляете ли вы по всему Казахстану?',
                'Да, мы доставляем по всем городам Казахстана через курьерские службы. '
                'Срок доставки — 1–5 рабочих дней в зависимости от региона.',
            ),
            (
                'Вся ли продукция оригинальная?',
                'Да, мы работаем только с официальными поставщиками и гарантируем '
                '100% оригинальность каждого продукта.',
            ),
            (
                'Можно ли получить консультацию по уходу?',
                'Конечно! Напишите нам в WhatsApp — наши специалисты бесплатно '
                'подберут уход под ваш тип кожи.',
            ),
            (
                'Какие способы оплаты доступны?',
                'Оплата при получении, Kaspi перевод, банковская карта. '
                'Подробности уточняйте при оформлении заказа.',
            ),
        ]

        FAQ.objects.all().delete()
        for i, (question, answer) in enumerate(faqs_data):
            FAQ.objects.create(question=question, answer=answer, order=i)

        self.stdout.write(self.style.SUCCESS('Демонстрационные данные успешно загружены!'))
