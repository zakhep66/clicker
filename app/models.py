from django.db import models


class Owner(models.Model):

    nick = models.CharField(max_length=50)
    total_data = models.BigIntegerField(default=0)

    class Meta:

        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    def __str__(self):
        return "Пользователь: {} с айди: {}".format(self.nick, self.id)
