from .models import Category
from core.models import SocialLink

def get_categories(request):
    all_categories = Category.objects.all()
    return dict(all_categories=all_categories)

def get_social_link(request):
    all_social_links = SocialLink.objects.all()
    return dict(social_links=all_social_links)

