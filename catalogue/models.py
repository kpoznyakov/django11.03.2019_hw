from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Item(models.Model):
    name_short = models.CharField(max_length=128)
    name_long = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
    )
    desc = models.TextField(
        blank=True,
        null=True,
    )
    params = models.TextField(
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    image = models.ImageField(
        upload_to='catalogue',
        blank=True,
        verbose_name='подпись',
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET(4),
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return str(self.id) + " | " + self.name_short + " | " + self.name_long
