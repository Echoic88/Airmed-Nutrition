import uuid
from django.db import models


# Create your models here.
class Brand(models.Model):
    """
    Model for food Brand names
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
