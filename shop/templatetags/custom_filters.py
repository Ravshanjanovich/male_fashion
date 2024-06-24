from django import template

register = template.Library()

@register.filter
def is_wishlist(product, request):
    return product in request.user.wishlist.all()
