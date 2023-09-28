from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import CustomerSerilizer

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerilizer(data, many=True)
    return JsonResponse({'customers': serializer.data})
    