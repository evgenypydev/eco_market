from django.urls import path, re_path
from .endpoints import OrderCreateAPIView, OrderUpdateAPIView, OrdersHistoryRetrieveAPIView, OrdersHistoryListAPIView



urlpatterns = [
    path('order/create/', OrderCreateAPIView.as_view()),
    re_path('order/update/(?P<pk>.+)/', OrderUpdateAPIView.as_view()),
    path('orders/history/', OrdersHistoryListAPIView.as_view()),
    re_path('order/(?P<pk>.+)/', OrdersHistoryRetrieveAPIView.as_view()),
]