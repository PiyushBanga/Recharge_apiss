from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Recharge(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    recharge_ammount = models.DecimalField(max_digits=10, decimal_places=2)
    recharge_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.plan)