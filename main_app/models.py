from django.db import models
from django.urls import reverse
# from datetime import date
from django.contrib.auth.models import User

# MEALS = (
#   ('B', 'Breakfast'),
#   ('L', 'Lunch'),
#   ('D', 'Dinner'),
# )
# Create your models here.
# class Toy(models.Model):
#   name = models.CharField(max_length=50)
#   color = models.CharField(max_length=20)

#   def __str__(self):
#     return self.name
  
#   def get_absolute_url(self):
#     return reverse('toys_detail', kwargs={'pk': self.id})
  
class Cat(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})

  # def fed_for_today(self):
  #   return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
  
# class Feeding(models.Model):
#   date = models.DateField('Feeding Date')
#   meal = models.CharField(
#     max_length=1,
#     choices=MEALS,
#     default=MEALS[0][0]
#   )
#   # Create a chat_id FK
#   chat = models.ForeignKey(
#     Chat,
#     on_delete=models.CASCADE
#   )
#   def __str__(self):
#     return f"{self.get_meal_display()} on {self.date}"
#   class Meta:
#     ordering = ['-date']

#   class Photo(models.Model):
#     url = models.CharField(max_length=200)
#     chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

#   def __str__(self):
#     return f"Photo for chat_id: {self.chat_id} @{self.url}"

# TAVY'S FORUM CODE    
#parent model
class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)
 
#child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)