from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from author.decorators import with_author


@with_author
class Company(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False)


@with_author
class Profile (TimeStampedModel):
    user = models.OneToOneField(User, related_name='profile')
    organization = models.ForeignKey(Company, related_name='users', null=False, blank=False)

    def __unicode__(self):
        return "User: " + str(self.user) + ", Organization: " + str(self.organization)
