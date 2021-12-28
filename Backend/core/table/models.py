from django.db import models

class Table(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    name = models.CharField(max_length=150, verbose_name="Название")
    amount = models.PositiveIntegerField(default=0, verbose_name="Количество")
    distance = models.PositiveIntegerField(default=0, verbose_name="Дистанция")

    def __str__(self):
        return f'{self.name} - {self.date}'

    class Meta:
        ordering = ['-date']
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'