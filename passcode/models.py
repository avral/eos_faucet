from random import randint

from django.db import models

from passcode.twilio import twilio


class PassRequest(models.Model):
    number = models.CharField(max_length=100, null=True)
    code = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{} <-> {}'.format(self.number, self.code)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = randint(10000, 99999)

            twilio.messages.create(
                to=self.number,
                from_='TravelChain',
                body=f'Hello from TravelChain. Your code: {self.code}'
            )

        super().save(*args, **kwargs)
