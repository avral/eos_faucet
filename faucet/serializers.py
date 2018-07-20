from rest_framework import serializers

from utils.eos import account_exists
from passcode.serializers import PassRequestValidateSerializer


class AccountCreateSerializer(PassRequestValidateSerializer):
    account = serializers.CharField(max_length=12)
    owner_pub = serializers.CharField(max_length=100)
    active_pub = serializers.CharField(max_length=100)
    # TODO Валидация ключей

    def validate_account(self, account):
        if account_exists(account):
            raise serializers.ValidationError('EOSIO account already exists')

        return account
