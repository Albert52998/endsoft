from django.db import models


class Soft(models.Model):
    '''Модель программы'''
    img = models.ImageField(verbose_name='Фото софта')
    title = models.CharField(max_length=60, verbose_name='Название софта')
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    counter = models.PositiveIntegerField(default=0, verbose_name='Кол-во загрузок')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Модерация')
    file = models.FileField(null=True, blank=True, upload_to='files/', verbose_name='Файл')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Софт'
        verbose_name_plural = 'Софты'
        ordering = ['-published']


class Category(models.Model):
    '''Модель категории программы'''
    img = models.FileField(null=True, blank=True, verbose_name='Фото категории')
    name = models.CharField(max_length=25, verbose_name='Название')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']


