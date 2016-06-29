from django.db import models

# Create your models here.
<<<<<<< 4fa556c9891804486c2ad5557d1dfc84aebd0906
=======

class ToDo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True)
>>>>>>> What
