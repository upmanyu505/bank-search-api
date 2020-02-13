from rest_framework import serializers
from api.models import BankList


class BankListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankList
        fields = [
            'id',
            'ifsc',
            'bank_id',
            'bank_name',
            'branch',
            'address',
            'city',
            'district',
            'state',
        ]


class BankListSerializerSearch(serializers.ModelSerializer):
    class Meta:
        model = BankList
        fields = [
            'ifsc',
            'bank_id',
            'branch',
            'address',
            'city',
            'district',
            'state',
        ]
