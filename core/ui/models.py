from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from multiselectfield import MultiSelectField


class Sliders(models.Model):
    title1 = models.CharField(max_length=100, null=True, blank=True, verbose_name='THE TOP LINE ')
    title2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='IN THE MIDDLE LINE')
    title3 = models.CharField(max_length=100, null=True, blank=True, verbose_name='LOWEST LINE')
    link = models.URLField(verbose_name='WEB SITE', null=True, blank=True)
    picture = models.ImageField('SELECTED IMAGE', null=True, blank=True)
    def __str__(self):
        return self.title1
    class Meta:
        verbose_name_plural = "SLIDERS"


class About(models.Model):
    img = models.ImageField('SELECTED IMAGE', null=True, blank=True)
    class Meta:
        verbose_name_plural = "AbOuT"

class Contact(models.Model):

    location = models.CharField(max_length=5500, help_text=(':2131/5 sokak no:6 Adalet mahallesi bayraklı'), verbose_name='LOCATION')
    countrylocation = models.CharField(max_length=5500, null=True, blank=True)
    phone = models.IntegerField(verbose_name='PHONE NUMBER')
    fax = models.IntegerField(verbose_name='FAX')
    email1 = models.EmailField(max_length=5100)
    web = models.URLField(max_length=5100)

    class Meta:
        verbose_name_plural = "ConTaCt"


class Agent(models.Model):
    jobType=(
        ('Real Estate Broker','Real Estate Broker'),
        ('Real Estate Agent','Real Estate Agent'),
    )
    experienceType=(
        ('years','years'),
        ('month','month'),
    )
    first_name = models.CharField(max_length=50, verbose_name='FIRST NAME')
    last_name = models.CharField(max_length=50, verbose_name='LAST NAME')
    job = models.CharField(max_length=150, choices=jobType, default='Real Estate Broker', verbose_name='JOB')
    img = models.ImageField(verbose_name='PICTURE')
    phoneNumber = models.IntegerField(verbose_name='PHONE NUMBER')
    email = models.EmailField(max_length=100, verbose_name='EMAIL ADRESS')
    facebook = models.URLField(null=True, blank=True, verbose_name='FACBOOK ADRESS')
    twitter = models.URLField(null=True, blank=True, verbose_name='TWITTER ADRESS')
    google_plus = models.URLField(null=True, blank=True, verbose_name='GOOGLE PLUSE ADRESS')
    linkedin = models.URLField(null=True, blank=True, verbose_name='LINKEDNI ADRESS')
    skypeid = models.CharField(max_length=200, null=True, blank=True, verbose_name='SKYPE ID')
    inDate = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='INDATE')
    biography = RichTextField(null=True, blank=True)
    discriptions = RichTextField(null=True, blank=True)
    workExperience = models.IntegerField(null=True, blank=True, verbose_name='WORK EXPERIENCE')
    experience = models.CharField(max_length=150, choices=experienceType, default='years', verbose_name='EXPERIENCE')
    status = models.BooleanField(default=True, verbose_name='to be seen ?')
    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
    class Meta:
        verbose_name_plural = "AgEnT"
class HomeName(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return str(self.name)

class House(models.Model):

    units=(
        ('₺','tl'),
        ('€','euro'),
        ('$','dollar')

    )
    type_of=(
        ('rent','rent'),
        ('sale','sale')
    )
    amenitiesChoices=(
        ('Air Conditioning','AirConditioning'),
        ('Bedding','Bedding'),
        ('Balcony','Balcony'),
        ('Cable TV','CableTV'),
        ('Internet','Internet'),
        ('Parking','Parking'),
        ('Lift','Lift'),
        ('Pool','Pool'),
        ('Dishwasher','Dishwasher'),
        ('Toaster','Toaster')
    )
    name = models.CharField(max_length=200, verbose_name='Home name')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True, verbose_name='AGENT')
    homeName = models.ForeignKey(HomeName, on_delete=models.CASCADE, null=True, blank=True, verbose_name='HoMeNaMe')
    price = models.IntegerField(verbose_name='PRICE')
    price_unit = models.CharField(max_length=150, choices=units, default='tl', verbose_name='PRICE UNITE')
    bathrooms = models.CharField(max_length=150, verbose_name='BATHROOMS')
    square = models.IntegerField(verbose_name='SQUARE')
    parking = models.CharField(max_length=150, verbose_name='GARAJE')
    rooms = models.CharField(max_length=150, verbose_name='ROOMS')
    kitchen = models.IntegerField(null=True, blank=True, verbose_name='KITCHEN')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='ADDRESS')
    type = models.CharField(max_length=150, choices=type_of,default='rent')
    amenities = MultiSelectField(choices=amenitiesChoices, verbose_name='AMENITIES', null=True, blank=True)
    descriptions=RichTextField(null=True, blank=True)
    inDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='ENTRY DATE')
    status = models.BooleanField(default=True, verbose_name='to be seen ?')
    # descriptions=RichTextField(verbose_name='descriptions details',null=True,blank=True)
    def __str__(self):
        return str(self.name) + ' ' + str(self.type)
    class Meta:
        verbose_name_plural = "House"

class FeaturesHome(models.Model):
    descriptions = RichTextField(null=True, blank=True)
    Furnished = models.TextField(verbose_name='Fully Furnished')
    Security = models.TextField(verbose_name='Non Stop Security')
    Design = models.TextField(verbose_name='Latest Interior Design')
    Fittings = models.TextField(verbose_name='Luxurious Fittings')
    LivingInside = models.TextField(verbose_name='Living Inside a Nature')
    RoyalTouchPaint = models.TextField(verbose_name='Royal Touch Paint')
    class Meta:
        verbose_name_plural = "Features Home"

class BrandsItem(models.Model):
    brandimg = models.ImageField(verbose_name='BRAND PICTURE')
    brandsName = models.CharField(max_length=200, null=True, blank=True, verbose_name='BRAND NAME')

class Service(models.Model):

    title = models.CharField(max_length=300, verbose_name='title', null=True, blank=True)
    descriptions = RichTextField(verbose_name='descriptions details', null=True, blank=True)
    summaryOfDescriptions = RichTextField( null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "SeRvIs"

class Blog(models.Model):
    homeName = models.ForeignKey(HomeName, on_delete=models.CASCADE, null=True, blank=True, verbose_name='HoMeNaMe')
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True, verbose_name='AGENT')
    descriptions = RichTextField(null=True, blank=True)
    descriptions2 = RichTextField(null=True, blank=True)
    aboutBuilding = RichTextField(null=True, blank=True)
    inDate = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='ENTRY DATE')
    status = models.BooleanField(default=True, verbose_name='to be seen ?')
    class Meta:
        verbose_name_plural = "New Building Design"


class Pictures(models.Model):
    homeName = models.ForeignKey(House, related_name="Pictures", verbose_name="resimler",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', verbose_name="resim seç")
    status = models.BooleanField(default=True,verbose_name='Gosterilsin mi?')
    cover = models.BooleanField(default=False,verbose_name='kapak resim mi?')
    def delete(self,*args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)
    class Meta:
        verbose_name_plural='Images for House'