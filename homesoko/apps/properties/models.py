from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem
from author.decorators import with_author
from autoslug import AutoSlugField
import django_filters
from sorl.thumbnail import get_thumbnail


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


class SalePropertiesManager(models.Manager):
    def get_query_set(self):
        return super(SalePropertiesManager, self).get_query_set().filter(category=SokoProperty.CategoryOptions.Sale)


class LettingPropertiesManager(models.Manager):
    def get_query_set(self):
        return super(LettingPropertiesManager, self).get_query_set().filter(category=SokoProperty.CategoryOptions.Sale)


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

    class StateOptions(DjangoChoices):
        New = ChoiceItem('new', 'New')
        Active = ChoiceItem('active', 'Active')
        Deleted = ChoiceItem('deleted', 'Deleted')

    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(_('Description'), blank=True, null=True)
    bedrooms = models.IntegerField(max_length=5, null=True, blank=True, choices=BedroomOptions.choices)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True, choices=BathroomsOptions.choices)
    structure_size = models.PositiveIntegerField(null=True, blank=True,
                                                 help_text='Size of the structure in square feet')
    lot_size = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True,
                                   help_text='Size of the lot in acres')
    city = models.ForeignKey(City, null=False, blank=False)
    neighbourhood = models.ForeignKey(Neighbourhood, null=False, blank=False)
    object = models.Manager()
    sale = SalePropertiesManager()
    letting = LettingPropertiesManager()

    def primary_image_thumbnail(self):
        return get_thumbnail(self.primary_image().file, '225x172', crop='center', quality=99)

    def primary_image(self):
        images = self.images.all()
        try:
            return images[0]
        except IndexError:
            # We return a dict with fields that mirror the key properties of
            # the ProductImage class so this missing image can be used
            # interchangably in templates.  Strategy pattern ftw!
            return {
                'original': self.get_missing_image(),
                'caption': '',
                'is_missing': True}


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
    file = models.ImageField(
        _("File"), upload_to="images", max_length=255)
    soko_property = models.ForeignKey(
        SokoProperty, related_name='images', verbose_name=_("Soko Property"))
    caption = models.CharField(
        _("Caption"), max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('soko_property', 'file')
        verbose_name = _('Property Image')
        verbose_name_plural = _('Property Images')

    def __unicode__(self):
        return u"Image of '%s'" % self.soko_property


class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = SokoProperty
        fields = ['neighbourhood', 'city', 'bedrooms', 'price']
