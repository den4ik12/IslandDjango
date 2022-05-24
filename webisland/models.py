from django.db import models


class Island(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name="Название", db_index=True)
    country = models.CharField(max_length=250, verbose_name="Страна")
    square = models.FloatField(verbose_name="Площадь")
    continent = models.CharField(verbose_name="Континент", max_length=300)

    class Meta:
        verbose_name = "Остров"
        verbose_name_plural = "Острова"

    def __str__(self):
        return self.title
