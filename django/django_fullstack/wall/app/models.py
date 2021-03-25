from django.db import models
from bcrypt import checkpw,hashpw,gensalt
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        s  = gensalt()
        self.password = hashpw(self.password.encode("utf8"), s).decode("utf8")
        super(User, self).save(*args,**kwargs)

class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")
    message = models.ForeignKey(to=Message, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
