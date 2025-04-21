from django.db import models
from userApp.models import Profile
from coreApp.models import CoreModel
from django.core.validators import MinValueValidator, MaxValueValidator


CITY_CHOICES = (
    ('Andijon', 'Andijon'),
    ('Namangan', 'Namangan'),
    ('Farg‘ona', 'Farg‘ona'),
    ('Toshkent', 'Toshkent'),
    ('Sirdaryo', 'Sirdaryo'),
    ('Jizzax', 'Jizzax'),
    ('Samarqand', 'Samarqand'),
    ('Qashqadaryo', 'Qashqadaryo'),
    ('Surxondaryo', 'Surxondaryo'),
    ('Buxoro', 'Buxoro'),
    ('Navoiy', 'Navoiy'),
    ('Xorazm', 'Xorazm'),
    ('Qoraqalpog‘iston', 'Qoraqalpog‘iston'),
)


class Category(CoreModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_image', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(CoreModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product_image", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.0)
    file = models.FileField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, choices=CITY_CHOICES)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}  -->  {self.user}'


class Connection(CoreModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} --> {self.project}'


class Comment(CoreModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.project}"


class Like(CoreModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    grade = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user} - {self.project}"
