from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True, blank=False, null=False, unique=True)
    fam = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=250, verbose_name='Имя')
    otc = models.CharField(max_length=250, blank=True, null=True, verbose_name='Отчество')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)


class Coord(models.Model):
    latitude = models.FloatField
    longitude = models.FloatField
    height = models.IntegerField()


class Level(models.Model):
    DIFFICULTY_LEVEL = (
        ('1A', '1A'),
        ('1Б', '1Б'),
        ('2A', '2A'),
        ('2Б', '2Б'),
        ('3A', '3A'),
        ('3Б', '3Б')
    )

    spring = models.CharField(max_length=2, choices=DIFFICULTY_LEVEL)
    summer = models.CharField(max_length=2, choices=DIFFICULTY_LEVEL)
    autumn = models.CharField(max_length=2, choices=DIFFICULTY_LEVEL)
    winter = models.CharField(max_length=2, choices=DIFFICULTY_LEVEL)


class PerevalAdded(models.Model):

    STATUS = (
        ('new', 'Запрос создан'),
        ('pending', 'Запрос на рассмотрении'),
        ('accepted', 'Запрос принят'),
        ('rejected', 'Запрос отклонен')
    )

    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100)
    connect = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    coords = models.ForeignKey(Coord, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Image(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    data = models.ImageField(upload_to="uploads/")
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, null=True, related_name='images')

    def __str__(self):
        return f'{self.pk} {self.title}'