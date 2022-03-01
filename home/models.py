from django.db import models

# Create your models here.
class staff(models.Model):
    staffName = models.CharField(primary_key=True,max_length=24)
    staffContactNumber = models.CharField(max_length=10)

    def __str__(self):
        return self.staffName
        # fnam mnma lnman status image gender username password