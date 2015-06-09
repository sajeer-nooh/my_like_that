from django.db import models
from django.contrib.auth.models import User


class AppUser(models.Model):
    user = models.OneToOneField(User, verbose_name=u'User', unique=True)
    fb_uid = models.CharField(max_length=100, null=True, blank=True) 
    tw_uid = models.CharField(max_length=100, null=True, blank=True) # Twitter User Id
    ig_uid = models.CharField(max_length=100, null=True, blank=True) # Instagram user id
    phone = models.CharField(max_length=20, unique=True)
    photo = models.CharField(max_length=255, null=True, blank=True)

#     def __unicode__(self):
#         if self.user.last_name:
#             return self.user.first_name + u' ' + self.user.last_name
#         if self.user.first_name:
#             return self.user.first_name
#         return 'Unknown'
