from django.db import models


class Message(models.Model):
    "A message sent from the contact form"
    name = models.CharField("Nom", max_length=255)
    email = models.EmailField("Email")
    body = models.TextField("Missatge")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '[%s] %s' % (self.timestamp, self.name)


class Interested(models.Model):
    "Someone who is interested in receiving info periodically via email"
    email = models.EmailField("Email")
    timestamp = models.DateTimeField(auto_now_add=True)
    added = models.BooleanField(default=False,
        help_text="Has been added to the mailing list?")

    def __unicode__(self):
        return '[%s] %s' % (self.timestamp, self.email)
        
