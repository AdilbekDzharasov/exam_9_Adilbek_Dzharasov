from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from webapp.managers import CustomManager


class Photo(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='pics',
        null=False,
        blank=False
    )
    sign = models.CharField(
        max_length=100,
        verbose_name='Подпись',
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='Автор',
        blank=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удален',
        default=False,
        null=False
    )

    object = CustomManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f"{self.author} -- {self.sign}"

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Chosen(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_chosen',
        verbose_name='Пользователь'
    )
    image = models.ForeignKey(
        to='webapp.Photo',
        on_delete=models.CASCADE,
        related_name='chosens',
        verbose_name='Избр. фотография'
    )

    class Meta:
        verbose_name = 'Избранная фотография'
        verbose_name_plural = 'Избранные фотографии'

