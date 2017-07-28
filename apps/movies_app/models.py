from __future__ import unicode_literals
from django.db import models
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "First name should be more than 2 characters"
        if len(postData['username']) < 2:
            errors["username"] = "Username should be more than 2 characters"
        if not re.match(EMAIL_REGEX, postData['email'] ):
            errors["email"] = "Email needs to be valid"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be 8 charcters or more"
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Password has to match confirmation'
        if str(postData['birth']) > str(datetime.date.today()):
            errors['birth'] = 'You havent been born yet?'
        if len(postData['zipCode']) != 5:
            errors['zipCode'] = 'Please enter a valid zip code'
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    zipCode = models.IntegerField()
    objects = UserManager()

class showTime(models.Model):
    time = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name= "User_showtimes")
    moveieID = models.IntegerField(default=0)
<<<<<<< HEAD
=======

>>>>>>> 897e12a1bb744ff52a6ad12ba9b3e1b6fcb13e17
