from django.db import models

# Create your models here.

class Pizza(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        #allows us to set a special attibute telling django to use toppings when referring to more than one
        verbose_name_plural = 'toppings'

    def __str__(self):
        return f"{self.text[:35]}..."

        
class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)      

    class Meta:
        #allows us to set a special attibute telling django to use toppings when referring to more than one
        verbose_name_plural = 'comments'

    def __str__(self):
        return f"{self.text[:35]}..."
