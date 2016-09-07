from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models


class QUser(models.Model):
    """
        Quser model class
    """

    MALE   = 'M'
    FEMALE = 'F'

    SEX_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )

    WHITE       = 'WHITE'
    INDIAN      = 'INDIAN'
    PAKISTANI   = 'PAKISTANI'
    BANGLADESHI = 'BANGLADESHI'
    ASIAN       = 'ASIAN'
    BLACK_CAR   = 'BLACK_CAR'
    BLACK_AFR   = 'BLACK_AFR'
    CHINESE     = 'CHINESE'
    OTHER       = 'OTHER'

    ETHN_CHOICES = (
        (WHITE      , 'WHITE'),
        (INDIAN     , 'INDIAN'),
        (PAKISTANI  , 'PAKISTANI'),
        (BANGLADESHI, 'BANGLADESHI'),
        (ASIAN      , 'ASIAN'),
        (BLACK_CAR  , 'BLACK_CAR'),
        (BLACK_AFR  , 'BLACK_AFR'),
        (CHINESE    , 'CHINESE'),
        (OTHER      , 'OTHER'),
    )

    age       = models.IntegerField(default=30, validators=[MinValueValidator(25), MaxValueValidator(84)])
    sex       = models.CharField(choices=SEX_CHOICES, default=MALE, max_length=10)
    ethnicity = models.CharField(choices=ETHN_CHOICES, default=WHITE, max_length=25)
    # # could be better using a specific control or
    # http://django-localflavor.readthedocs.io/en/latest/localflavor/gb/#localflavor.gb.forms.GBPostcodeField
    postcode  = models.CharField(null=True, blank=True, max_length=6)


class QUserInfo(models.Model):
    """
        Clinical info about Quser
    """

    NON_SMOKER   = 'NON-SMOKER'
    EX_SMOKER    = 'EX-SMOKER'
    LIGHT_SMOKER = 'LIGHT-SMOKER'
    MOD_SMOKER   = 'MOD-SMOKER'
    HEAVY_SMOKER = 'HEAVY-SMOKER'

    SMOKER_CHOICES = (
        (NON_SMOKER  , 'NON-SMOKER'),
        (EX_SMOKER   , 'EX-SMOKER'),
        (LIGHT_SMOKER, 'LIGHT-SMOKER'),
        (MOD_SMOKER  , 'MOD-SMOKER'),
        (HEAVY_SMOKER, 'HEAVY-SMOKER'),
    )

    NONE   = ''
    T1     = 'T1'
    T2     = 'T2'

    DIABETES_CHOICES = (
        (NONE, 'NONE'),
        (T1, 'T1'),
        (T2, 'T2'),
    )

    user            = models.OneToOneField(QUser, primary_key=True, on_delete=models.CASCADE)
    smoking_status  = models.CharField(default=NON_SMOKER, choices=SMOKER_CHOICES, max_length=25)
    diabetes_status = models.CharField(default=NONE, choices=DIABETES_CHOICES, max_length=5)
    heart_attacked_relative = models.BooleanField('Angina or heart attack in a 1st degree relative < 60',
                                                  default=False)
    kidney_disease  = models.BooleanField('Chronic kidney disease (stage 4 or 5)', default=False)
    atrial_fibrillation = models.BooleanField(default=False)
    blood_pressure_treat = models.BooleanField(default=False)
    rheumatoid_arthritis = models.BooleanField(default=False)
    cholesterol_hdl_ratio = models.DecimalField(null=True, decimal_places=1, max_digits=4,
                                                validators=[MinValueValidator(1.0), MaxValueValidator(12.0)])
    blood_pressure = models.IntegerField(null=True, validators=[MinValueValidator(70), MaxValueValidator(210)])
    height = models.IntegerField(null=True, validators=[MinValueValidator(140), MaxValueValidator(210)])
    weight = models.IntegerField(null=True, validators=[MinValueValidator(40), MaxValueValidator(180)])
