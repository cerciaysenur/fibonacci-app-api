from django.urls import path
from .views import FibonacciView

urlpatterns = [
    path('<int:n>/', FibonacciView.as_view(), name='fibonacci'),
]
