from django.db import models
from django.contrib.auth.models import User

class TODOO(models.Model):
    srno = models.AutoField(primary_key=True)   # unique ID for each task
    title = models.CharField(max_length=255)    # task title
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link to logged-in user
    date = models.DateTimeField(auto_now_add=True)  # auto-set when created
    completed = models.BooleanField(default=False)  # mark task as done

    def __str__(self):
        return self.title