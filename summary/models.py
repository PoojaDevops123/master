from django.db import models

# Create your models here.


class User_Model(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_Name = models.CharField(max_length=50)
    user_DOB = models.CharField(max_length=50)
    user_Gender = models.BooleanField(default=False)
    user_Email = models.EmailField(max_length=254)

    user_Mobile = models.CharField(max_length=10)
    user_UserName = models.CharField(max_length=50)
    user_PWD = models.CharField(max_length=250)
    user_is_Active = models.BooleanField(default=False)

    class Meta:
        db_table = "user_tbl"
