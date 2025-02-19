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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    

class News(models.Model):
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.poster.username} - {self.title}"