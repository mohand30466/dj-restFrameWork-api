from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    country = models.TextField(max_length=50)
    profissional = models.TextField(max_length=50)
    # Date_of_birth = models.DateField(default='2020')
    telephone = models.IntegerField(default=0)
    profilebic = models.ImageField(null=True, blank=True)
    # age = models.IntegerField()


    def __str__(self):
        return self.user.username




class Movies(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField(max_length=350)
    def num_of_rating(self):

        ratings = Rates.objects.filter(movie=self)
        print("test ratings", ratings)
        return len(ratings)
   
    def average_of_rating(self):
        sum = 0
        ratings = Rates.objects.filter(movie=self) 
        for rate in ratings:
            sum += rate.stars
            if rate.stars > 0:
                return sum/len(ratings)
               
            else:
                return 0
    


class Rates(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    class Meta:
        unique_together = (("user", "movie"),)
        index_together = (("user", "movie"),)
