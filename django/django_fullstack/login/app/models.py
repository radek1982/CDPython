from django.db import models
from bcrypt import hashpw, checkpw, gensalt
import re

class UserManager(models.Manager):
    def validate_registration(self, data):
       
        errors = []
        required ={"first_name": {"min": 2}, "last_name": {"min": 2}, "email": {"min": 2}, "password": {"min":8}, "password-confirm": {"min":8} }
        for r in required:
            if not r in data or len(data[r]) == 0:
                errors.append(f"{r.capitalize()} is required")
        self.validate_email(data, errors)

        self.validate_passwords(data, errors)
        return errors

    def validate_email(self, data, errors):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data['email']):    # test whether a field matches the pattern            
            errors.append("Invalid email address!")

    def validate_passwords(self, data, errors):
        pwd =data["password"]
        pc = data["password-confirm"]
        if len(pwd)<8:
            errors.append("Password needs to be at least 8 characters long")
        if (pwd !=pc):
            errors.append("Password needs to match confirmation!")


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = UserManager()
    def save(self, *args, **kwargs):
        salt = gensalt()
        self.password = hashpw(password=self.password.encode("utf8"), salt=salt).decode("utf8")
        super(User, self).save(*args, **kwargs)

    def login(email, password):

        try:
         u = User.objects.filter(email = email).first()
         if u:
             if checkpw(password.encode("utf8"), u.password.encode("utf8")):
                 return u

        except Exception:
            raise
    

