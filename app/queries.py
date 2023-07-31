from django.db.models import Count
from .models.locations import Locations

cat_list = Locations.objects.values('category').annotate(count=Count('category')).order_by()


def get_location(cat):
    loc = Locations.objects.filter(category=cat)
    return loc
