from django.db import models

# Create your models here.
class Airport(models.Model):

    CITIES = (('Montreal', 'Montreal'), ('Toronto', 'Toronto'), ('Ottawa', 'Ottawa'), ('Vancouver', 'Vancouver'), ('Calgary', 'Calgary'))
    #   (('YUL': En base,'Montreal':Displayed))

    city = models.CharField(max_length=15, choices=CITIES)
    airport = models.CharField(max_length=255, default='name of the airport')
    acronym = models.CharField(max_length=3, default='___')


    def __str__(self):
        return '{}{}{}'.format(self.city, self.airport, self.acronym)




