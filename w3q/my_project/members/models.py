from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True, blank=True)
  joined_date = models.DateField(null=True, auto_now_add=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname} <{self.phone}>"
  
class FormModel(models.Model):
  title=models.CharField(max_length=300)
  description=models.TextField()
  last_modified=models.DateTimeField(auto_now_add=True)
  img=models.ImageField(upload_to="Images/")

  def __str__(self):sx
    return self.title


#  ADD HERE
class LoginUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
