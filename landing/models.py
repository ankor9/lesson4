from django.db import models

# Create your models here.

class EmailCollector(models.Model):
    class Meta:
        db_table = 'emails'
        verbose_name = 'email'
        verbose_name_plural = 'emails'
    first_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='First Name')
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Last Name')
    email = models.EmailField(max_length=60, blank=False, null=False, verbose_name='E-mail')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
