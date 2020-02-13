from django.contrib.postgres.search import SearchQuery, SearchVector
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from api.models import BankList
from api.serializers import BankListSerializerSearch



class bank_autocomplete(generics.ListAPIView):
    model = BankList
    serializer_class = BankListSerializerSearch

    def get_queryset(self):
        queryset = BankList.objects
        qstr = self.request.query_params.get('q', None)
        limit = self.request.query_params.get('limit', None)
        offset = self.request.query_params.get('offset', None)

        if qstr is not None:
            queryset = queryset.filter(branch__search=qstr).order_by('ifsc')

        if limit is not None:
            queryset = queryset[:limit]
        
        if offset is not None:
            queryset = queryset[offset:]
        
        return queryset


class bank_search(generics.ListAPIView):
    model = BankList
    serializer_class = BankListSerializerSearch

    def get_queryset(self):
        vector = SearchVector(
            'ifsc', 
            'bank_id', 
            'branch',
            'address',
            'city',
            'district',
            'state',
            'bank_name'
        )
        query = SearchQuery(self.request.query_params.get('q', None))
        queryset = BankList.objects.annotate(search=vector)
        limit = self.request.query_params.get('limit', None)
        offset = self.request.query_params.get('offset', None)

        if query is not None:
            queryset = queryset.filter(search=query).order_by('ifsc')

        if limit is not None:
            queryset = queryset[:int(limit)]
        
        if offset is not None:
            queryset = queryset[int(offset):]
        
        return queryset