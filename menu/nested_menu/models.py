from django.db import models


class Menu(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Заголовок меню'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='Слаг меню'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class Thing(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок предмета')
    slug = models.SlugField(
        max_length=255,
        verbose_name="Слаг предмета"
    )
    menu = models.ForeignKey(
        Menu,
        blank=True,
        related_name='things',
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='childrens',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.title
