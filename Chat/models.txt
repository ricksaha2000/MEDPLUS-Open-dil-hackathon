from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    auth = models.ForeignKey(Authority, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(blank = True, null = True, max_length = 100)

    def __str__(self):
        return self.writer.username + self.auth.authUser.username