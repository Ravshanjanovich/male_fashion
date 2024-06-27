from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from .validators import PhoneValidators

class UserManager(BaseUserManager):

    def __created_user(self, phone, password, **kwargs):
        phone = PhoneValidators.clean(phone)
        validator = PhoneValidators()
        validator(phone)

        user = UserModel(**kwargs)
        user.phone = phone
        user.set_password(password)

        user.save()

    def create_user(self, *args, **kwargs):
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)

        if kwargs.get("is_staff") or kwargs.get("is_superuser"):
            raise Exception("User is_staff=False va is_superuser=False Bo'lishi shart")
        
        return self.__created_user(*args, **kwargs)
    
    def create_superuser(self, *args, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if not kwargs.get("is_staff") or not kwargs.get("is_superuser"):
            raise Exception("User is_staff=True va is_superuser=True Bo'lishi shart")
        
        return self.__created_user(*args, **kwargs)
    
    def get_by_natural_key(self, username):
        return UserModel.object.get(username=username)
    
class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=13, validators=[PhoneValidators()], unique=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
        
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups_set',  
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups'),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profiles')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=125, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=6, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'