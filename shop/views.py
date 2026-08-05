from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, FAQ, Product, Review, SiteSettings


def _get_site_settings():
    return SiteSettings.get_settings()


def index(request):
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:6]
    reviews = Review.objects.filter(is_active=True)[:6]
    faqs = FAQ.objects.filter(is_active=True)[:5]
    context = {
        'featured_products': featured_products,
        'reviews': reviews,
        'faqs': faqs,
        'site_settings': _get_site_settings(),
        'page_title': 'Главная',
        'meta_description': _get_site_settings().site_description,
    }
    return render(request, 'shop/index.html', context)


def catalog(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)
    category_slug = request.GET.get('category', '')
    search_query = request.GET.get('q', '').strip()

    if category_slug:
        products = products.filter(category__slug=category_slug)

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query)
            | Q(short_description__icontains=search_query)
            | Q(description__icontains=search_query)
        )

    context = {
        'categories': categories,
        'products': products,
        'active_category': category_slug,
        'search_query': search_query,
        'site_settings': _get_site_settings(),
        'page_title': 'Каталог',
        'meta_description': 'Каталог корейской косметики KOKO Kazakhstan. '
        'Очищение, сыворотки, кремы, SPF, тонеры и маски.',
    }
    return render(request, 'shop/catalog.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True,
    ).exclude(pk=product.pk)[:4]

    context = {
        'product': product,
        'related_products': related_products,
        'site_settings': _get_site_settings(),
        'page_title': product.name,
        'meta_description': product.short_description,
    }
    return render(request, 'shop/product_detail.html', context)
