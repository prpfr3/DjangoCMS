from django.db import models
from django.conf import settings


class MilitaryVehicleClass(models.Model):
    mvclass = models.CharField(max_length=100, default=None, blank=True, null=True)
    wikislug = models.SlugField(
        max_length=250, allow_unicode=True, default=None, blank=True, null=True
    )
    description = models.CharField(max_length=500, default=None, blank=True, null=True)
    notes = models.TextField(default=None, blank=True, null=True)
    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="Fav", related_name="favorite_things"
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Military Vehicle Class"
        verbose_name_plural = "Military Vehicle Classes"
        managed = False


class Fav(models.Model):
    thing = models.ForeignKey(MilitaryVehicleClass, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favs_users"
    )

    # https://docs.djangoproject.com/en/3.0/ref/models/options/#unique-together
    class Meta:
        unique_together = ("thing", "user")
        verbose_name = "Military Vehicle Favourite"
        verbose_name_plural = "Military Vehicle Favourites"

    def __str__(self):
        return f"{self.user.username} likes {self.thing.mvclass[:10]}"
