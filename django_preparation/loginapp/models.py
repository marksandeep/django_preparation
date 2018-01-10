from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    auth_user = models.OneToOneField(User)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=500, null=True)



