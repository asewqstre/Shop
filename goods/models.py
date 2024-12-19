from django.db import models
from users.models import Users
from django.core.validators import MaxValueValidator


class Goods(models.Model):
    """
    An abstract class for everything for sale in shop
    """

    name = models.CharField(max_length=50)
    article = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    seller = models.ForeignKey(to=Users, on_delete=models.CASCADE, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, validators=[MaxValueValidator(5, 'Rate points cannot be greater than 5')])
    reviews = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Wearings(Goods):
    """
    An abstract class for everything people can dress up
    """

    SEASONS = [
        ('Summer', 'Summer'),
        ('Demi-season', 'Demi-season'),
        ('Winter', 'Winter')
    ]

    STYLES = [
        ('Classic', 'Classic'),
        ('Casual', 'Casual'),
        ('Street', 'Street'),
        ('Mini', 'Minimalist')
    ]

    season = models.CharField(max_length=11, choices=SEASONS)
    style = models.CharField(max_length=10, choices=STYLES)

    class Meta:
        abstract = True


class Clothes(Wearings):
    """
    An abstract class for all clothes
    """

    SIZES = [
        ('XXS', '2Extra Small'),
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large'),
        ('XXL','2Extra Large'),
    ]

    SEX = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    COLOR = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Brown', 'Brown'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Gray', 'Gray'),
    ]

    COMPOSITION = [
        ('Cotton', 'Cotton'),
        ('')
    ]

    size = models.CharField(max_length=3, choices=SIZES, null=True)
    sex = models.CharField(max_length=6, choices=SEX, null=True)
    color = models.CharField(max_length=5, choices=COLOR, null=True) 

    class Meta:
        abstract = True


class Shoes(Wearings):
    """
    An abstract class for all shoes
    """

    SIZES = [
        (30, 30),
        (31, 31),
        (32, 32),
        (33, 33),
        (34, 34),
        (35, 35),
        (36, 36),
        (37, 37),
        (38, 38),
        (39, 39),
        (40, 40),
        (41, 41),
        (42, 42),
        (43, 43),
        (44, 44),
        (45, 45),
        (46, 46),
        (47, 47),
        (48, 48),
        (49, 49),
        (50, 50),
    ]

    SEX = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex')
    ]

    COLOR = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Brown', 'Brown'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Gray', 'Gray'),
    ]

    size = models.IntegerField(choices=SIZES, null=True)
    sex = models.CharField(max_length=6, choices=SEX, null=True)
    color = models.CharField(max_length=5, choices=COLOR, null=True)

    class Meta:
        abstract = True


class T_shirts(Clothes):
    """
    Model for T-shirts
    """

    class Meta:
        db_table = 'T-shirts'
        verbose_name = 'T-shirt'


class Skirts(Clothes):
    """
    Model for Skirts
    """

    sex = models.CharField(max_length=6, default='Female', editable=False)
    length = models.DecimalField(max_digits=3, decimal_places=1, validators=[MaxValueValidator(200)], verbose_name='length in cantimeters')

    class Meta:
        db_table = 'Skirts'
        verbose_name = 'Skirt'