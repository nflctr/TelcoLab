from django.db import models

# Create your models here.
class Informations(models.Model):
  judul = models.CharField(max_length=50)
  tipe  = models.CharField(max_length=50)
  isi   = models.TextField()
  created = models.DateTimeField(auto_now_add= True)
  updated = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.judul

# class Post(models.Model):
#   title = models.CharField(max_length=100)
#   body = models.TextField()

#   def str(self):
#       return "{}".format(self.title)

# class Modul(models.Model):
#   title = models.CharField(max_length=50)
#   category = models.CharField(max_length=50)
#   body = models.TextField()

#   def str(self):
#     return "{}".format(self.title)
