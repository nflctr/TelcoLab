from django.db import models
from tinymce.models import HTMLField
# Create your models here.

# Kategori : Artikel (textField), Materi (charField), Gambar (imgField)
# class Kategori(models.Model):
#   name = models.CharField(max_length=40, null=False, blank=False)
#   def __str__(self):
#     return self.name

# Materi : Semua judul modul di TelcoLab (charField)
# class Materi(models.Model):
#   name = models.CharField(max_length=40, null=False, blank=False)
#   def __str__(self):
#     return self.name

class Informations(models.Model):
  # kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)
  # materi = models.ForeignKey(Materi, on_delete=models.SET_NULL, null=True, blank=True)
  judul = models.CharField(max_length=50)
  tipe  = models.CharField(max_length=50)
  isi   = models.TextField()
  created = models.DateTimeField(auto_now_add= True)
  updated = models.DateTimeField(auto_now = True)
  content = HTMLField()
  class Meta:
    ordering = ('judul',)
  def __str__(self):
    return self.judul



