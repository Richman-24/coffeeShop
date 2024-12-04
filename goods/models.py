from django.db import models

ADMIN_NAME_LIMIT = 20


class BaseGoodsModel(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=86, unique=True, verbose_name="URL")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        abstract = True
        ordering = ('name',)

class Category(BaseGoodsModel):
    class Meta(BaseGoodsModel.Meta):
        db_table = "category"
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self) -> str:
        return self.name[:ADMIN_NAME_LIMIT]


class Product(BaseGoodsModel):
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=4, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка в %"
    )
    amount = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name="category",
        verbose_name="Категория",
    )

    class Meta(BaseGoodsModel.Meta):
        db_table = "product"
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self) -> str:
        return f"{self.name[:ADMIN_NAME_LIMIT]}, {self.amount}"
