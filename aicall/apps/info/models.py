from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

class Country(models.Model):
    name_ru = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
    
    def __str__(self):
        return self.name_ru

class Language(models.Model):
    name_ru = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
    
    def __str__(self):
        return self.name_ru

class Education(models.Model):
    name_ru = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'
    
    def __str__(self):
        return self.name_ru

class ActionArea(models.Model):
    name_ru = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Сфера деятольности'
        verbose_name_plural = 'Сферы деятольности'
    
    def __str__(self):
        return self.name_ru

class TalkThemes(models.Model):
    name_ru = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)

    image_png = ProcessedImageField(
        verbose_name='ImagePNG',
        processors=[ResizeToFill(600, 600)],
        format='PNG',
        options={'quality': 100},
        null=True,
        blank=True
    )
    
    image_svg = models.FileField(
        verbose_name='ImageSVG',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Темы для разговора'
        verbose_name_plural = 'Темы для разговоров'
    
    def __str__(self):
        return self.name_ru

class PositiveSide(models.Model):
    name_ru = models.CharField("Positive side ru", max_length=255)
    name_eng = models.CharField("Positive side eng", max_length=255)

    class Meta:
        verbose_name = 'позитивная сторона'
        verbose_name_plural = 'позитивные стороны'
    
    def __str__(self):
        return self.name_ru
class NegativeSide(models.Model):
    name_ru = models.CharField("Negative side ru", max_length=255)
    name_eng = models.CharField("Negative side eng", max_length=255)

    class Meta:
        verbose_name = 'негативная сторона'
        verbose_name_plural = 'негативные стороны'
    
    def __str__(self):
        return self.name_ru