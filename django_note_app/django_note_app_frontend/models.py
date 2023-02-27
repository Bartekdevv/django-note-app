from django.db import models
from django.utils.timezone import now


class Field(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.description


class Note(models.Model):
    id = models.BigAutoField(primary_key=True)
    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        default=Field.objects.get(description="General"),
    )
    text = models.TextField()
    created_at = models.DateField(auto_now=True)
