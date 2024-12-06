from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from users.validators import validate_title_year

EMAIL_LENGTH_LIMIT = NAME_LENGTH_LIMIT = 30
ADMIN_TEXT_LIMIT = 20

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создание суперпользователя с email вместо username."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class UserRole(models.TextChoices):
        USER = "user", "пользователь"
        MODERATOR = "moderator", "модератор"
        ADMIN = "admin", "администратор"
    email = models.EmailField(max_length=EMAIL_LENGTH_LIMIT, unique=True)
    birth_data = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения", validators=(validate_title_year,)
    )
    is_active = models.BooleanField(default=True, verbose_name="Доступность")
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER,
        verbose_name="Роль",
    )
    # phone = models.CharField(max_length=10, blank=True, null=True)  # Не забыть валидатор номера телефона
    
    objects = CustomUserManager()

    class Meta:
        db_table = "user"
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("last_name", "first_name")

    def __str__(self) -> str:
        return self.get_full_name()[:ADMIN_TEXT_LIMIT]

    @property
    def is_moderator(self):
        return self.role == self.UserRole.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.UserRole.ADMIN or self.is_superuser or self.is_staff
