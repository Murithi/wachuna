from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem
from author.decorators import with_author
from autoslug import AutoSlugField
from sorl.thumbnail import get_thumbnail
from django_states.fields import StateField
from django_states.machine import StateMachine, StateDefinition, StateTransition


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
        return super(SalePropertiesManager, self).get_query_set().filter(state=PropertyStateMachine.STATE_PUBLISHED, category=Property.CategoryOptions.Sale)


class LettingPropertiesManager(models.Manager):
    def get_query_set(self):
        return super(LettingPropertiesManager, self).get_query_set().filter(state=PropertyStateMachine.STATE_PUBLISHED, category=Property.CategoryOptions.Letting)

@with_author
class Feature(TimeStampedModel):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class PropertyStateMachine(StateMachine):
    log_transitions = True
    # States Constants
    STATE_NEW = 'new'
    STATE_FEATURES_ADDED = 'features_added'
    STATE_IMAGES_ADDED = 'images_added'
    STATE_AWAITING_ADMIN_APPROVAL = 'awaiting_admin_approval'
    STATE_PUBLISHED = 'published'
    STATE_INACTIVATED = 'inactivated'

    # Possible states
    class new(StateDefinition):
        description = _('A newly created property')
        initial = True

    class features_added(StateDefinition):
        description = _('Features have been added to the property')

    class images_added(StateDefinition):
        description = _('Images have been added to the property')

    class awaiting_admin_approval(StateDefinition):
        description = _('Admin needs to approve this property to be updated')

    class published(StateDefinition):
        description = _('The property has been published')

    class inactivated(StateDefinition):
        description = _('The property is inactive')

    # State transitions
    class mark_features_added(StateTransition):
        from_state = ['new', 'images_added']
        to_state = 'features_added'
        description = 'Mark this property that the features have been added'

    class mark_images_added(StateTransition):
        from_state = ['new', 'images_added']
        to_state = 'images_added'
        description = 'Mark this property that the images have been added'

    class mark_awaiting_admin_approval(StateTransition):
        from_state = ['images_added', 'features_added']
        to_state = 'awaiting_admin_approval'
        description = 'Mark this property as awaiting the admin approval'

    class mark_published(StateTransition):
        from_state = ['awaiting_admin_approval', 'published']
        to_state = 'awaiting_admin_approval'
        description = 'Mark this property as published'

    class mark_inactivated(StateTransition):
        from_state = ['new', 'images_added', 'features_added', 'awaiting_admin_approval', 'published']
        to_state = 'inactivated'
        description = 'Mark this property as inactivated'


@with_author
class Property(TimeStampedModel):
    class PropertyTypeOptions(DjangoChoices):
        Apartment = ChoiceItem('apartment', 'Apartment')
        House = ChoiceItem('house', 'House')
        Office = ChoiceItem('office', 'Office')
        Land = ChoiceItem('land', 'Land')
        Townhouse = ChoiceItem('townhouse', 'Townhouse')

    class CategoryOptions(DjangoChoices):
        Letting = ChoiceItem('letting', 'Letting')
        Sale = ChoiceItem('sale', 'For Sale')

    class BedroomOptions(DjangoChoices):
        One = ChoiceItem(1, '1')
        Two = ChoiceItem(1, '2')
        Three = ChoiceItem(3, '3')
        Four = ChoiceItem(4, '4')
        Five = ChoiceItem(5, '5')
        Six = ChoiceItem(6, '6')
        Seven = ChoiceItem(7, '7')
        Eight = ChoiceItem(8, '8')
        Nine = ChoiceItem(9, '9')
        Ten = ChoiceItem(10, '10')
        Eleven = ChoiceItem(11, '11')
        Twelve = ChoiceItem(12, '12')
        Thirteen = ChoiceItem(13, '13')
        Fourteen = ChoiceItem(14, '14')
        Fifteen = ChoiceItem(15, '15')

    class BathroomsOptions(DjangoChoices):
        all_ensuite = ChoiceItem('all_ensuite', 'All Ensuite')
        One = ChoiceItem('1', '1')
        Two = ChoiceItem('2', '2')
        Three = ChoiceItem('3', '3')
        Four = ChoiceItem('4', '4')
        Five = ChoiceItem('5', '5')
        Six = ChoiceItem('6', '6')

    name = models.CharField(max_length=20, blank=False)
    slug = AutoSlugField(populate_from='name')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(_('Description'), blank=True, null=True)
    bedrooms = models.IntegerField(max_length=5, null=True, blank=True, choices=BedroomOptions.choices)
    bathrooms = models.CharField(max_length=15, null=True, blank=True, choices=BathroomsOptions.choices)
    structure_size = models.PositiveIntegerField(null=True, blank=True,
                                                 help_text='Size of the structure in square feet')
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                   help_text='Size of the lot in acres')
    city = models.ForeignKey(City, null=False, blank=False)
    neighbourhood = models.ForeignKey(Neighbourhood, null=False, blank=False)
    category = models.CharField(max_length=14, blank=True, choices=CategoryOptions.choices)
    property_type = models.CharField(max_length=20, blank=True, choices=PropertyTypeOptions.choices)
    agency = models.ForeignKey(User, null=False, blank=False, related_name='property')
    features = models.ManyToManyField(Feature, related_name='property', null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    state = StateField(machine=PropertyStateMachine, default='new')
    objects = models.Manager()
    sale = SalePropertiesManager()
    letting = LettingPropertiesManager()

    class Meta:
        verbose_name_plural = 'Properties'

    @property
    def status_percentage(self):
        status_percentage = 0

        if self.state == PropertyStateMachine.STATE_PUBLISHED:
            status_percentage = 100
        else:
            if self.features.all():
                status_percentage += 50
            if self.images.all():
                status_percentage += 30

        return status_percentage

    @property
    def details(self):
        beds = self.bedrooms if self.bedrooms else '-'
        baths = self.bathrooms if self.bathrooms else '-'
        return "Price: %d,Category: %s,Type: %s,Location: %s-%s,Beds: %s,Baths: %s" % (self.price, self.category, self.property_type, self.neighbourhood, self.city, beds, baths)

    def primary_image_thumbnail(self):
        if self.primary_image():
            return get_thumbnail(self.primary_image().file, '225x225', crop='center', quality=99)
        return None

    def slider_image(self):
        if self.primary_image():
            return get_thumbnail(self.primary_image().file, '1400x600', crop='center', quality=99)
        return None

    def get_missing_image(self):
        pass

    def primary_image(self):
        images = self.images.filter(deleted=False)
        try:
            return images[0]
        except IndexError:
            return None


class PropertyImage(TimeStampedModel):
    file = models.ImageField("File", upload_to="images", max_length=255)
    property = models.ForeignKey(Property, related_name='images', verbose_name=_("Property"))
    caption = models.CharField(_("Caption"), max_length=200, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('property', 'file')
        verbose_name = _('Property Image')
        verbose_name_plural = _('Property Images')

    def __unicode__(self):
        return u"Image of '%s'" % self.property

    def delete(self):
        self.deleted = True
        self.save()

