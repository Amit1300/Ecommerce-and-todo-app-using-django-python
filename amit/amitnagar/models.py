from django.db import models
import datetime

  # Create your models here.
# creating a form  
class Todolist(models.Model):
    title=models.CharField(max_length=50)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

class Employee(models.Model):
      employ_id=models.IntegerField()
      firstname=models.CharField(max_length=50)
      lastname=models.CharField(max_length=50)


      def __str__(self):
            return self.firstname

class Category(models.Model):
      name=models.CharField(max_length=500)
     


      def __str__(self):
            return self.name
    
class Product(models.Model):
      price=models.IntegerField(default=0)
      discription=models.CharField(max_length=500,default="")
      name=models.CharField(max_length=500)
      image=models.ImageField(upload_to="upload/products")
      category= models.ForeignKey(Category, on_delete=models.CASCADE,default=1)


      def __str__(self):
            return self.name




class Customer(models.Model):
      name=models.CharField(max_length=500)
      phone_no=models.CharField(max_length=500)
      email=models.EmailField(max_length=254)
      password=models.CharField(max_length=50,default=0)


      def __str__(self):
            return self.name

class Order(models.Model):
      product=models.ForeignKey(Product,on_delete=models.CASCADE)
      customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
      quantity=models.IntegerField(default=1)
      price=models.IntegerField()
      phone=models.CharField( max_length=50)
      address=models.CharField(max_length=500)
      date=models.DateField(default=datetime.datetime.today)


      def placeorder(self):
            self.save()








