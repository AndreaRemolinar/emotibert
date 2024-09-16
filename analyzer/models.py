from django.db import models

# Create your models here.
# modèle de base de données pour stocker les sentiments et les emojis correspondants

class Sentiment(models.Model):
    sentiment_label = models.CharField(max_length=50)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return self.sentiment_label
