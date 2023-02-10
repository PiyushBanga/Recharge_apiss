from django.urls import path
from .views import PlanListAPIView, RechargeAPIView

urlpatterns = [
    path('plans/', PlanListAPIView.as_view(), name='plan-list'),
    path('recharge/', RechargeAPIView.as_view(), name='recharge'),
]