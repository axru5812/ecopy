from django.db import models
import numpy as np


# CATEGORY CLASSES
# -----------------------------------------------------------------------------
class BaseCategory(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    income_type = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseCategory):
    pass


class SubCategory(BaseCategory):
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)


# TRANSACTION CLASSES
# -----------------------------------------------------------------------------
class Transaction(models.Model):
    amount = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.DateField()

    class Meta:
        abstract = True

    @property
    def rounded_amount(self):
        return np.round(self.amount)


class Income(Transaction):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Expense(Transaction):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
