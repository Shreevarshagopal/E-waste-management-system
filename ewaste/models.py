from django.db import models

# Create your models here.

class Registration(models.Model):
    username=models.CharField(max_length=30)
    mobnum=models.IntegerField()
    mail=models.EmailField()
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    cat_name=models.CharField(max_length=30)
    cat_img=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cat_name
    
class Waste_mat(models.Model):
    cat_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    waste_name=models.CharField(max_length=50)

    def __str__(self):
        return self.waste_name
    
class Total_cat(models.Model):
    waste_name=models.ForeignKey(Waste_mat,on_delete=models.CASCADE,db_column='title')
    cat_name=models.ForeignKey(Category,on_delete=models.CASCADE,db_column='category_name')
    waste_use=models.CharField(max_length=1000,db_column='waste_name')
    waste_cost=models.IntegerField(db_column='waste_cost')
