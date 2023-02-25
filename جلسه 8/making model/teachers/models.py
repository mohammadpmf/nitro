from django.db import models


class Teacher(models.Model):
    # noe 1 (hatman be hame gofteh beshe)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nat_code = models.CharField(max_length=10)
    age = models.IntegerField()
    description = models.TextField()

    # noe 2 (bad az in ke noe 1 ro hazm kardan, gofte beshe.)
    decimal_age = models.DecimalField(max_digits=10, decimal_places=3)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"Teacher name is: {self.name} {self.surname}"

    # # noe 3 (ezafe ha. lazem nist be hame gofteh beshe. age khoob bood gorooh gofteh beshe)
    # boolean = models.BooleanField()
    # real_age = models.PositiveIntegerField()
    # float_age = models.FloatField()
    # slug = models.SlugField()
    # time = models.TimeField()
    # birth_day = models.DateField()
    # ip = models.GenericIPAddressField()
    # email = models.EmailField()
    # url = models.URLField()
    # # image = models.ImageField() # اگه ننویسیم مستقیم تو خود پوشه اپ آپلود میکنه.
    # image = models.ImageField(upload_to='media')
    # # file_field_test = models.FileField() # اگه ننویسیم مستقیم تو خود پوشه اپ آپلود میکنه.
    # file_field_test = models.FileField(upload_to='file haye man')
    # register_date = models.DateTimeField(auto_now_add=True)
    # registeration_update_date = models.DateTimeField(auto_now=True)
    # blank_name = models.CharField(max_length=50, blank=True) # blank is for validation
    # null_name = models.CharField(max_length=50, null=True) # null is db related
    # blank_null_name = models.CharField(max_length=50, blank=True, null=True)

    # # noe 4 (ezafe tar. lazem nist be hich kas gofte she. khodam khastam yad begiram.)
    # # models.IntegerChoices
    # class AgeGroup(models.IntegerChoices):
    #     KIDS = 12
    #     TEENAGER = 15
    #     ADULT = 18
    #     GROWN_UP = 25
    #     OLD = 40
    #     ELDER = 70
    # age_group=models.IntegerField(choices=AgeGroup.choices)
    # binary = models.BinaryField()
    # count = models.Count(expression='salam')
    