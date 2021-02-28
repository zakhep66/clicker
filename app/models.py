from django.db import models


class Owner(models.Model):

    nick = models.CharField(max_length=50)
    total_data = models.BigIntegerField(default=0)

    class Meta:

        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    def __str__(self):
        if self.id == 1:
            return 'Admin Nike: "{}"'.format(self.nick)
        elif self.id == 2:
            return 'Admin Nick: "{}", ID: "{}"'.format(self.nick, self.id)
        else:
            return 'Nick: "{}", ID: "{}"'.format(self.nick, self.id)
