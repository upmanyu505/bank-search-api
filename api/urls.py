from django.urls import path
from api.views import bank_autocomplete, bank_search


urlpatterns = [
    path('branches/autocomplete/', bank_autocomplete.as_view(), name='autocomplete'),
    path('branches/', bank_search.as_view(), name='search')
]
