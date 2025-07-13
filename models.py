from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    # addres = models.CharField(max_length=100)
    sity = models.CharField(max_length=50)
    nomer = models.CharField(max_length=5)
    ulica = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)

    def __str__(self):
        return self.name

MY_CHOICES = (
        ('1', 'Галерия'),
        ('2', 'Промоция'),
        ('3', 'Въпрос'),
        ('4', 'Друго'),
    )

class Nav(models.Model):
    name = models.CharField(max_length=50)
    page_type = models.CharField(max_length=5, choices=MY_CHOICES, default='1')
    in_footer = models.BooleanField()
    on_nav = models.BooleanField()
    page_id = models.IntegerField()

    def __str__(self):
        return self.name

class EmptyPage(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name
class Galery(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)
    in_nav = models.IntegerField()

    def __str__(self):
        return self.name

class Promotion(models.Model):
    name = models.CharField(max_length=50)
    from_price = models.FloatField()
    to_price = models.FloatField()
    img_url = models.CharField(max_length=100)
    in_nav = models.IntegerField()
    in_index = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    in_nav = models.IntegerField()

    def __str__(self):
        return self.question