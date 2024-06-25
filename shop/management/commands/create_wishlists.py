from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shop.models import WishList

class Command(BaseCommand):
    help = "Yo'q foydalanuvchilar uchun istaklar ro'yxatini yaratadi"

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            if not hasattr(user, 'wishlist'):
                WishList.objects.create(user=user)
                self.stdout.write(self.style.SUCCESS(f"Foydalanuvchi uchun istaklar ro'yxati yaratildi{user.username}"))
