from django.db import models

# Create your models here.
class Tasklist(models.Model):
    task=models.CharField( max_length=100)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.task+"."+str (self.done)

