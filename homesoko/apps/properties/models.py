from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem
from author.decorators import with_author

@with_author
class City(TimeStampedModel):
    name = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return self.name


@with_author
class Neighbourhood(TimeStampedModel):
    name = models.CharField(max_length=20)
    city = models.ForeignKey(City, null=False, blank=False)

    def __unicode__(self):
        return self.name


@with_author
class SokoProperty(TimeStampedModel):
    class PropertyTypeOptions(DjangoChoices):
        Land = ChoiceItem('land', 'Land')
        Apartment = ChoiceItem('apartment', 'Apartment')

    class CategoryOptions(DjangoChoices):
        Letting = ChoiceItem('letting', 'Letting')
        Sale = ChoiceItem('sale', 'For Sale')

    class BedroomOptions(DjangoChoices):
        One = ChoiceItem(1, '1')
        Two = ChoiceItem(1, '2')

    class BathroomsOptions(DjangoChoices):
        One = ChoiceItem(1, '1')
        OneAndHalf = ChoiceItem(1.5, '1 and 1/2')
        Two = ChoiceItem(2, '2')
        TwoAndHalf = ChoiceItem(2.5, '2 and 1/2')

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(_('Description'), blank=True, null=True)
    bedroom = models.IntegerField(max_length=5, null=True, blank=True, choices=BedroomOptions.choices)
    bathroom = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True, choices=BathroomsOptions.choices)
    structure_size = models.PositiveIntegerField(null=True, blank=True,
                                                 help_text='Size of the structure in square feet')
    lot_size = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True,
                                   help_text='Size of the lot in acres')
    city = models.ForeignKey(City, null=False, blank=False)
    neighbourhood = models.ForeignKey(Neighbourhood, null=False, blank=False)


@with_author
class Features(TimeStampedModel):
    name = models.CharField(max_length=20)
    soko_property = models.ManyToManyField(SokoProperty, related_name='features', null=True, blank=True)

    def __unicode__(self):
        return self.name


class PropertyImage(TimeStampedModel):
    """
    An image of a property
    """
    soko_property = models.ForeignKey(
        SokoProperty, related_name='images', verbose_name=_("Soko Property"))
    original = models.ImageField(
        _("Original"), upload_to=settings.IMAGE_FOLDER, max_length=255)
    caption = models.CharField(
        _("Caption"), max_length=200, blank=True, null=True)

    #: Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField(_("Display Order"), default=0,
        help_text=_("""An image with a display order of
                       zero will be the primary image for a product"""))

    class Meta:
        unique_together = ("soko_property", "display_order")
        ordering = ["display_order"]
        verbose_name = _('Property Image')
        verbose_name_plural = _('Property Images')

    def __unicode__(self):
        return u"Image of '%s'" % self.property

    def is_primary(self):
        """
        Return bool if image display order is 0
        """
        return self.display_order == 0

    def resized_image_url(self, width=None, height=None, **kwargs):
        return self.original.url

    @property
    def fullsize_url(self):
        """
        Returns the URL path for this image.  This is intended
        to be overridden in subclasses that want to serve
        images in a specific way.
        """
        return self.resized_image_url()

    @property
    def thumbnail_url(self):
        return self.resized_image_url()

