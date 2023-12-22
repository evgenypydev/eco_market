from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderCreateUpdateSerializer, OrderListRetrieveSerializer
import phonenumbers


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer


class OrderUpdateAPIView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer


class OrdersHistoryListAPIView(ListAPIView):
    serializer_class = OrderListRetrieveSerializer

    def get_queryset(self):
        phone_number = self.request.data["phone_number"]
        return Order.objects.filter(phone_number=phone_number)


class OrdersHistoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = OrderListRetrieveSerializer

    def get_queryset(self):
        phone_number = self.request.data["phone_number"]
        return Order.objects.filter(phone_number=phone_number)


