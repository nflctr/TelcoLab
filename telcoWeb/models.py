from django.db import models
from tinymce.models import HTMLField

# Create your models here.

# Type : Artikel (textField), Materi (charField), Gambar (imgField)
class Type(models.Model):
  name = models.CharField(max_length=40, null=False, blank=False)
  def __str__(self):
    return self.name

# Modul : Semua judul modul di TelcoLab (charField)
class Modul(models.Model):
  name = models.CharField(max_length=40, null=False, blank=False)
  def __str__(self):
    return self.name

# Information : Semua database intinya ada di sini
class Information(models.Model):
  kategori = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)
  modul = models.ForeignKey(Modul, on_delete=models.SET_NULL, null=True, blank=True)
  title = models.CharField(max_length=50)
  desc  = models.CharField(max_length=50)
  image = models.ImageField(null=True, blank=True)
  content = HTMLField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add= True)
  updated = models.DateTimeField(auto_now = True)
  class Meta:
    ordering = ('materi','title')
  def __str__(self):
    return self.title



