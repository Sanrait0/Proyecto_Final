from django.db import models

# Create your models here.
from django.db import models


#class ProductCategory(models.Model):
#    state = models.CharField(max_length=256)
#    county = models.CharField(max_length=64)


class ConevalProyectoModel(models.Model):
    state = models.CharField(max_length=256)
    county = models.CharField(max_length=64)
    pct_pob = models.DecimalField(decimal_places=2, max_digits=15)
    #product_category = models.ForeignKey("products.ProductCategory", on_delete=models.CASCADE)

"""STATES = {
    (1, "Aguascalientes"),
    (2, "Baja California"),
    (3, "Baja California Sur"),
    (4, "Campeche"),
    (5, "Coahuila de Zaragoza"),
    (6, "Colima"),
    (7, "Chiapas"),
    (8, "Chihuahua"),
    (9, "Ciudad de México"),
    (10, "Durango"),
    (11, "Guanajuato"),
    (12, "Guerrero"),
    (13, "Hidalgo"),
    (14, "Jalisco"),
    (15, "México"),
    (16, "Michoacán de Ocampo"),
    (17, "Morelos"),
    (18, "Nayarit"),
    (19, "Nuevo León"),
    (20, "Oaxaca"),
    (21, "Puebla"),
    (22, "Querétaro"),
    (23, "Quintana Roo"),
    (24, "San Luis Potosí"),
    (25, "Sinaloa"),
    (26, "Sonora"),
    (27, "Tabasco"),
    (28, "Tamaulipas"),
    (29, "Tlaxcala"),
    (30, "Veracruz de Ignacio de la Llave"),
    (31, "Yucatán"),
    (32, "Zacatecas"),
}

class ConevalProyectoModel(models.Model):
    state = models.FloatField(default=1, choices=STATES)"""