#
#  FILE:     models.py
#  AUTHOR:   Group 1-3
#  DATE:     23 March 2015
#  DOES-COMPILE: True
#  DESCRIPTION:  This is a Django models file that corresponds to the CHF case DCD.
#
#  TODO:  In its current state, this is only a preliminary version.
#

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# To install the local flavor package, run the command "pip install django-localflavor" in your terminal.
# To install the imagefield field, run the command "pip install pillow".
from localflavor.us.us_states import US_STATES
from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField, USSocialSecurityNumberField
import datetime


class Address(models.Model):

    '''
        A user's location. Can be used to ship items or make payments.
    '''
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=30, null=True)
    state = USStateField(choices=US_STATES, default='')
    zip_code = USZipCodeField(max_length=5, null=True, blank=True)

    class Meta:
        ordering = ['state', 'city', 'zip_code', 'address1', 'address2']
        verbose_name_plural = 'addresses'

    def __str__(self):
        return '{} {} {}, {}  {}'.format(self.address1, self.address1, self.city, self.state, self.zip_code)


class Photograph(models.Model):

    '''
        A photograph file with some additional metadata. Can be used to
        document items held by the foundation, people working for the
        Foundation, etc..
    '''
    date_taken = models.DateTimeField(null=True)
    place_taken = models.TextField(max_length=30, null=True)
    description = models.TextField(max_length=200, null=True)
    image = models.CharField(max_length=200, null=True)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username, email=self.normalize_email(email),)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

    # Redefine basic user fields
    username = models.CharField(
        unique=True, max_length=20, validators=[alphanumeric])
    email = models.EmailField(
        verbose_name='email address', unique=True, max_length=255)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)

    profile_image = models.ImageField(upload_to='/user/uploads/profile', blank=False, null=False,
                                      default="/static/app_account/media/default_profile.jpg")
    security_question = models.CharField(max_length=60, null=True)
    security_answer = models.CharField(max_length=30, null=True)
    requires_reset = models.BooleanField(default=False)
    phone = PhoneNumberField(max_length=12, null=True)
    organization_name = models.CharField(max_length=100, null=True)
    bio_sketch = models.CharField(max_length=200, null=True)
    emergency_contact_relationship = models.CharField(
        max_length=30, null=True)
    emergency_contact = models.ForeignKey(
        'self', related_name='+', blank=True, null=True)

    address = models.ForeignKey(
        Address, related_name='+', blank=True, null=True)
    id_photo = models.ForeignKey(
        Photograph, related_name='+', blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.username

    def get_groups(self):
        return self.groups

    def __unicode__(self):
        return self.get_full_name()


class Employee(User):

    '''
        A user authorized to act on behalf of the Foundation to handle
        transactions.
    '''
    date_hired = models.DateTimeField(null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    wage = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class Vendor(User):

    '''
        Any individual who sells items through the Foundation, whether at
        events or through the online store.
    '''
    SSN = USSocialSecurityNumberField(null=True)
    EIN = models.CharField(max_length=10, null=True)
    UTTaxID = models.CharField(max_length=10, null=True)
    sales_tax_return_form_given = models.BooleanField(default=False)


class Category(models.Model):

    '''
        Category within the product catalog.
    '''
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.description


class Clothing_Detail(models.Model):

    '''
        This contains all of the additional information that might be needed
        when dealing with an article of clothing.
    '''
    size = models.TextField(max_length=100, null=True)
    size_modifier = models.TextField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    color = models.CharField(max_length=10, null=True)
    pattern = models.TextField(max_length=100, null=True)
    start_year = models.IntegerField(max_length=10, null=True)
    end_year = models.IntegerField(max_length=10, null=True)


class Item(models.Model):

    '''
        A product in our inventory. This class represents any item
        that is held by the foundation, even if it is not for sale or rent.
    '''
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=300, null=True)
    serial_number = models.TextField(max_length=100, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    owner = models.ForeignKey(User, related_name='+', null=True)
    photo = models.ForeignKey(Photograph, related_name='+')
    category = models.ManyToManyField(Category, related_name='+', null=True)
    clothing_detail = models.ForeignKey(
        Clothing_Detail, related_name='+', null=True)

    real_type = models.ForeignKey(ContentType, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.real_type = self._get_real_type()
        super(Item, self).save(*args, **kwargs)

    def _get_real_type(self):
        return ContentType.objects.get_for_model(type(self))

    def cast(self):
        return self.real_type.get_object_for_this_type(pk=self.pk)


class Store_Item(Item):

    '''
        An item that can be found in the store. This class acts as a parent class
        for sale product and rentable article and is not intended to be initialized
        or accessed directly by any other class.
    '''
    quantity_on_hand = models.IntegerField(max_length=10, null=True)
    shelf_location = models.TextField(max_length=100, null=True)
    order_file = models.TextField(max_length=100, null=True)


class Sale_Product(Store_Item):

    '''
        Any product commonly sold in the store. This conrete class is intended to
        represent bulk products or products made by artisans that don't required
        customization.
    '''
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    manufacturer = models.CharField(max_length=100, null=True)

    creator = models.ForeignKey(Vendor, null=True)


class Custom_Product(Sale_Product):

    '''
        A product made by an artisan and customized according to a user's
        specifications.
    '''
    production_time = models.CharField(max_length=100, null=True)
    required_info = models.TextField(max_length=300, null=True)


class Order_Form(models.Model):

    '''
        An order form for a custom product. The information string holds
        all of the details that an artisan might need when making a custom
        product.
    '''
    customer_info = models.TextField(max_length=300, null=True)


class Rentable_Article(Store_Item):

    '''
        Any item in the Foundation's inventory that they are willing to rent out.
    '''
    price_per_day = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    condition_new = models.BooleanField(default=False)
    notes = models.TextField(max_length=300, null=True)


class Transaction(models.Model):

    '''
        Used to track the exchange of goods between an individual and the foundation
        via the website or in person. Can encompass rentals, sales, or fees.
    '''
    date = models.DateTimeField(default=datetime.date.today())
    phone = models.CharField(max_length=12, null=True)
    date_packed = models.DateTimeField(null=True)
    date_shipped = models.DateTimeField(null=True)
    tracking_number = models.TextField(max_length=30, null=True)

    payment_processed_by = models.ForeignKey(
        'User', related_name='paymentprocessedby', null=True, blank=True)
    ships_to = models.ForeignKey(
        'Address', related_name='+', null=True, blank=True)
    shipped_by = models.ForeignKey(
        'User', related_name='shippedby', null=True, blank=True)
    handled_by = models.ForeignKey(
        'User', related_name='handledby', null=True, blank=True)
    customer = models.ForeignKey('User', related_name='orders')


class Transaction_Item(models.Model):

    '''
        Abstract base class for line items in a transaction.  A line item can be one
        of sale item, fee, rental item, or service item.
    '''

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    transaction = models.ForeignKey('Transaction')

    class Meta:
        abstract = True


class Payment(Transaction_Item):

    '''
        An exchange of funds between an individual and the Foundation.
    '''
    date_paid = models.DateTimeField(null=True)


class Sale(Transaction_Item):

    '''
        A sale item for either a bulk or a serialized product.
    '''
    quantity = models.IntegerField()
    order_form = models.ForeignKey(
        Order_Form, related_name='+', null=True)

    sale_item = models.ForeignKey(Sale_Product)

    def __str__(self):
        return '{} {}'.format(self.amount, self.quantity)

    def get_custom_product_info(self):
        return self.order_form.customer_info


class Rental(Transaction_Item):

    '''
        Represents the rental of a single article.
    '''
    date_out = models.DateTimeField(null=True)
    date_due = models.DateTimeField(null=True)
    discount_percent = models.DecimalField(
        max_digits=3, decimal_places=2, null=True)

    rental_item = models.ForeignKey(Rentable_Article)


class Rental_Return(models.Model):

    '''
        Represents the return of one rented item.
    '''
    return_condition = models.TextField(max_length=200, null=True)
    date_returned = models.DateTimeField(null=True)

    rental = models.ForeignKey(Rental, related_name='return_instance')
    handled_by = models.ForeignKey(
        'User', related_name='rentalhandledby', null=True, blank=True)


class Fee(Transaction_Item):

    '''
        Abstract base class for the various fee types.  Concrete fee types
        include late and damage fees.  The maximum fee amount should be the purchase
        price of the rental product less the rental fee.
    '''
    waived = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Late_Fee(Fee):

    '''
        A late fee for an item rental. This is a concrete subclass of Fee.
        For now we use the daily rental price as the per-day late fee.
    '''
    days_late = models.PositiveIntegerField()
    rental_return = models.ForeignKey(
        Rental_Return, related_name='late_fee_set')

    def __str__(self):
        return '{} {} {}'.format(self.amount, self.days_late, self.waived)


class Damage_Fee(Fee):

    '''
        A damage fee for an item rental. This is a concrete subclass of Fee.
    '''
    description = models.TextField()
    rental_return = models.ForeignKey(
        Rental_Return, related_name='damage_fee_set')

    def __str__(self):
        return '{} {} {}'.format(self.amount, self.description, self.waived)


class Expected_Sale_Item(models.Model):

    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)

    photo = models.ForeignKey(Photograph, related_name='+', null=True)


class Public_Event(models.Model):

    '''
        A public event such as "The Colonial Heritage Festival".
    '''
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)


class Event(models.Model):

    '''
        An instance of a public event, such as "The 2015 Colonial Heritage Festival at Orem".
    '''
    start_date = models.DateField()
    end_date = models.DateField()
    map_file_name = models.TextField(max_length=200)
    venue_name = models.TextField(max_length=200)
    address = models.ForeignKey(Address, related_name='+')
    discount_code = models.CharField(max_length=7)

    public_event = models.ForeignKey(Public_Event)


class Area(models.Model):

    '''
        An area of an event may represent an exhibit, a first aid station, or some other
        distinct element within the event.
    '''
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    place_number = models.PositiveIntegerField()

    coordinator = models.ForeignKey(User, related_name='coordinates')
    supervisor = models.ForeignKey(User, related_name='supervises')
    event = models.ForeignKey(Event)
    participants = models.ManyToManyField('User', through='Role')


class Historical_Figure(models.Model):

    '''
        A historical figure that a participant may portray at an event.
    '''
    name = models.TextField(max_length=200)
    birth_date = models.DateField(null=True)
    birth_place = models.TextField(max_length=200, null=True, blank=True)
    death_date = models.DateField(null=True)
    death_place = models.TextField(max_length=200, null=True, blank=True)
    biographical_note = models.TextField()
    is_fictional = models.BooleanField(default=False)


class Role(models.Model):

    '''
        This class identifies the relationship between a user who is a participant and
        the area(s) in which s/he participates.
    '''
    name = models.TextField(max_length=200)
    type = models.TextField(max_length=40)

    participant = models.ForeignKey('User')
    area = models.ForeignKey('Area')
    historical_figure = models.ForeignKey(Historical_Figure)
