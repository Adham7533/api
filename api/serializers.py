from rest_framework import serializers
from taxi.models import Taxis,Account


class TaxisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Taxis

        fields = ['name', 'lasname', 'surname', 'phone', 'email', 'number', 'brand', 'color', 'license']
class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields='__all__'