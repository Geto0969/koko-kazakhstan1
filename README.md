# KOKO Kazakhstan — Интернет-магазин корейской косметики

Современный интернет-магазин корейской косметики на Django с premium minimalism дизайном.

## Технологии

- **Backend:** Python 3.10+, Django 5+
- **Frontend:** HTML5, CSS3, JavaScript
- **База данных:** SQLite (для разработки)
- **Шаблоны:** Django Templates

## Структура проекта

```
koko-kazakhstan/
├── manage.py
├── requirements.txt
├── README.md
├── koko_project/              # Настройки Django-проекта
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── shop/                      # Основное приложение
    ├── admin.py               # Админ-панель
    ├── models.py              # Модели (товары, категории, отзывы, FAQ)
    ├── views.py               # Представления
    ├── urls.py                # URL-маршруты
    ├── context_processors.py  # Глобальные настройки сайта
    ├── management/
    │   └── commands/
    │       └── load_sample_data.py  # Загрузка демо-данных
    ├── static/shop/
    │   ├── css/main.css       # Стили
    │   └── js/main.js         # JavaScript
    └── templates/shop/
        ├── base.html
        ├── index.html         # Главная
        ├── catalog.html       # Каталог
        ├── product_detail.html # Карточка товара
        └── partials/          # Переиспользуемые блоки
```

## Быстрый старт

### 1. Открыть проект в PyCharm

1. Запустите PyCharm
2. **File → Open** → выберите папку `koko-kazakhstan`
3. PyCharm автоматически определит Django-проект

### 2. Создать виртуальное окружение (рекомендуется)

```bash
cd koko-kazakhstan
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Применить миграции и загрузить данные

```bash
python manage.py migrate
python manage.py load_sample_data
```

### 5. Создать суперпользователя (опционально, для админки)

```bash
python manage.py createsuperuser
```

### 6. Запустить сервер

```bash
python manage.py runserver
```

Откройте в браузере: **http://127.0.0.1:8000/**

Админ-панель: **http://127.0.0.1:8000/admin/**

## Настройка

### WhatsApp и контакты

В админ-панели (**Настройки сайта**) можно изменить:

- Номер WhatsApp (формат: `77001234567`)
- Ссылку на Instagram
- Адрес и время работы
- SEO title и description

### Добавление товаров

1. Войдите в админ-панель
2. Создайте категории (если нужны новые)
3. Добавьте товары с фото (URL изображения), описанием и ценой

## Страницы

| URL | Описание |
|-----|----------|
| `/` | Главная — баннер, популярные товары, отзывы, FAQ |
| `/catalog/` | Каталог с фильтрами и поиском |
| `/product/<slug>/` | Карточка товара с заказом через WhatsApp |
| `/admin/` | Админ-панель Django |

## Категории

- Очищение
- Сыворотки
- Кремы
- SPF
- Тонеры
- Маски

## Лицензия

Проект создан для KOKO Kazakhstan.
