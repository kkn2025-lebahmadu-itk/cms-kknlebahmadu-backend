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
    thumbnail = models.ImageField(upload_to='thumbnail', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.poster} - {self.title}"
    

class Complaint(models.Model):
    class StatusChoices(models.TextChoices):
        SELESAI = "selesai", "Selesai"
        PROGRESS = "progress", "Dalam Progress"
        TIDAK_VALID = "tidak_valid", "Tidak Valid"
        SUDAH_DIBACA = "sudah_dibaca", "Sudah Dibaca"
        PENDING = "pending", "Menunggu Konfirmasi"

    user = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.content[:10]}"
    
class Profile(models.Model):
    class TypeChoices(models.TextChoices):
        INTI = "inti", "Informasi Inti"
        TAMBAHAN = "tambahan", "Informasi Tambahan"

    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    type = models.CharField(
        max_length=20,
        choices=TypeChoices.choices
    )

    def __str__(self):
        return f"{self.key} - {self.value}"

class Gallery(models.Model):
    path = models.ImageField(upload_to='gallery/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.path} - {self.created_at}"
    

class Report(models.Model):
    pdf = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.path} - {self.created_at}"