from .models import Category


def get_categories(request):
    all_categories = Category.objects.all()
    return dict(all_categories=all_categories)