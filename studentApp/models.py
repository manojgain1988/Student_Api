from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    age=models.IntegerField()
    address=models.TextField()
    institute=models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural =("Student")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Student_detail", kwargs={"pk": self.pk})
