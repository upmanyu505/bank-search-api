from django.db.models import Model, CharField, IntegerField


class BankList(Model):
    ifsc = CharField(max_length=11, blank=False, null=True)
    bank_id = IntegerField(blank=False, null=True)
    branch = CharField(max_length=50, blank=False, null=True)
    address = CharField(max_length=150, blank=False, null=True)
    city = CharField(max_length=40, blank=False, null=True)
    district = CharField(max_length=40, blank=False, null=True)
    state = CharField(max_length=40, blank=False, null=True)
    bank_name = CharField(max_length=100, blank=False, null=True)
