from rest_framework import generics
from rest_framework.filters import SearchFilter
from taxi.models import Taxis,Account
from .serializers import TaxisSerializers,AccountSerializers

class TaxisAPIView(generics.ListAPIView):


    queryset = Taxis.objects.all()
    serializer_class = TaxisSerializers

    filter_backends = [SearchFilter]
    search_fields=['name','lasname','surname','phone','email','number','brand','color','license']
class AccountAPIView(generics.ListAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializers

    filter_backends = [SearchFilter]
    search_fields=['login','email','password']
