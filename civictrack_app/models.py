from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):

    CATEGORY_CHOICES = [
        ('Potholes', 'Potholes'),
        ('Garbage', 'Garbage'),
        ('Water Leakage', 'Water Leakage'),
        ('Broken Street Light', 'Broken Street Light'),
        ('Drainage', 'Drainage'),
        ('Public Safety', 'Public Safety'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    location = models.CharField(max_length=255)

    image = models.FileField(
        upload_to='issues/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    resolution_note = models.TextField(
        blank=True,
        null=True
    )

    resolution_image = models.FileField(
        upload_to='resolutions/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

# Create your models here.
