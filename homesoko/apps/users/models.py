from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from author.decorators import with_author
from userena.models import UserenaBaseProfile


@with_author
class Profile(TimeStampedModel, UserenaBaseProfile):
    user = models.OneToOneField(User, related_name='profile')
    company = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return "User: " + str(self.user) + ", Company: " + str(self.company)
