from django.db import models
import uuid

class BaseModel(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta():
        abstract=True


