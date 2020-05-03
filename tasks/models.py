from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Category(models.Model):
    slug = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} ({self.slug})'

class Priority(models.Model):

    PRIORITY_CHOICES = [
        ("High Priority", "Высокий приоритет"),
        ("Medium Priority", "Средний приоритет"),
        ("Low Priority", "Низкий приоритет"),
    ]

    name = models.CharField(max_length=128,
        choices=PRIORITY_CHOICES, default="Medium Priority"
        )
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    description = models.TextField("Описание")
    is_completed = models.BooleanField("Выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=u'Владелец',
        )
    category = models.ManyToManyField(
    	Category,
    	verbose_name=u'Категория',
    	blank=True
    	)
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        verbose_name=u'Приоритет',
        blank=True
        )

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.description.lower()

    def get_absolute_url(self):
        return reverse("tasks:details", args=[self.pk])
