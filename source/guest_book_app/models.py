from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


# Create your models here.

class StatusChoice(TextChoices):
    ACTIVE = ('active', 'Активна')
    BLOCKED = ('blocked', 'Заблокировано')

class Guest(models.Model):
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name="Автор")
    mail = models.EmailField(max_length=254, null=False, verbose_name="Электронная почта")
    text = models.TextField(max_length=3000, null=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    status = models.CharField(verbose_name='Статус', choices=StatusChoice.choices, max_length=20, default=StatusChoice.ACTIVE)
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.author} - {self.mail}"