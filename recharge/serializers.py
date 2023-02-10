from rest_framework import serializers
from .models import Plan, Recharge

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'name', 'description', 'price', 'validity')

class RechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recharge
        fields = ('id', 'plan','phone_number', 'recharge_ammount'  ,'recharge_date')
