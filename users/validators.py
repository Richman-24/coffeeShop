from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_title_year(value):
    """
    Валидация года произведения.
    Проверяет, что возраст участника от 6 до 99 лет.
    """
    value = value.year
    if value < timezone.now().year - 5 or value > timezone.now().year:
        raise ValidationError("Недопустимая дата.")