from django.db import models
import numpy as np


# Create your models here.
class Category(models.Model):
    name = models.CharField()
    color = models.CharField()

    class Meta:
        abstract = True


class IncomeCategory(Category):
    pass


class ExpenseCategory(Category):
    pass


class Transaction(models.Model):
    amount = models.FloatField()
    name = models.Charfield(max_length=100)
    description = models.Charfield(max_length=300)
    date = models.DateField()

    class Meta:
        abstract = True

    @property
    def rounded_amount(self):
        return np.round(amount)


class Income(Transaction):
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)


class Expense(Transaction):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
