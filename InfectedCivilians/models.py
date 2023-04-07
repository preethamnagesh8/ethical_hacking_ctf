from django.db import models

class InfectedCivilian(models.Model):
    name = models.CharField(max_length=100)
    infection_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    ZOMBIE_STATUS_CHOICES = [
        ('infected', 'Infected'),
        ('turned', 'Turned'),
        ('cured', 'Cured'),
    ]
    status = models.CharField(max_length=10, choices=ZOMBIE_STATUS_CHOICES, default='infected')

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
