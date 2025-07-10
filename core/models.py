from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Profile(models.Model):
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=120)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(blank=True, upload_to="pictures/%Y/%m/")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
