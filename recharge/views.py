from rest_framework import generics
from .models import Plan, Recharge
from .serializers import PlanSerializer, RechargeSerializer

class PlanListAPIView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class RechargeAPIView(generics.ListCreateAPIView):
    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer

    # def perform_create(self, serializer):
    #     plan = Plan.objects.get(id=self.request.data.get('plan_id'))
    #     serializer.save(plan=plan)