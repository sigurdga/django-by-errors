from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('food-detail', [self.id])

class Recipe(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to="pictures", blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('recipe-detail', [self.slug])

MEASUREMENT_CHOICES = (
    (1, "Piece"),
    (2, "Liter"),
    (3, "Cup"),
    (4, "Tablespoon"),
    (5, "Teaspoon"),
)

class Ingredient(models.Model):
    food = models.ForeignKey(Food)
    amount = models.DecimalField(decimal_places=2, max_digits=4)
    measurement = models.SmallIntegerField(choices=MEASUREMENT_CHOICES)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return "%.2f %s %s" % (self.amount, self.get_measurement_display(), self.food)

