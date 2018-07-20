from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=12, unique=True)
    number = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_created = models.BooleanField(default=False)
    err_msg = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'
