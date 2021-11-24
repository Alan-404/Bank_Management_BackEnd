from rest_framework import serializers
from bank_card.models import BankCardModel

class BankCardSerializer (serializers.ModelSerializer):
    class Meta:
        model = BankCardModel
        fields = "__all__"