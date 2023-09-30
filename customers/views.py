from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerilizer

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerilizer(data, many=True)
    return JsonResponse({'customers': serializer.data})
    

def customer(request, id):
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        raise Http404('Customer does not found')
    serializer = CustomerSerilizer(data)
    return JsonResponse({'customer': serializer.data})
    