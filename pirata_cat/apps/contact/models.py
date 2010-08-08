from django.db import models


class Message(models.Model):
    name = models.CharField("Nom", max_length=255)
    email = models.EmailField("Email")
    body = models.TextField("Missatge")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '[%s] %s' % (self.timestamp, self.name)

