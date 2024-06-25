from django import template

register = template.Library()

@register.simple_tag
def get_current_price(request, index):
    price_range = request.GET.get('price', '').split(';')
    if index < len(price_range):
        return price_range[index]
    return ''


@register.filter
def is_wishlist(product, request):
    try:
        wishlist = request.user.wishlist
        return wishlist.items.filter(product=product).exists()
    except wishlist.DoesNotExist:
        return False



