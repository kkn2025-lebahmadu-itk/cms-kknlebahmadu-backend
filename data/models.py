from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=[("user", "User"), ("admin", "Admin"), ("superuser", "Superuser")],
        default="user",
    )

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups", 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions", 
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email