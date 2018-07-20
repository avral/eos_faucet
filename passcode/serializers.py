from datetime import datetime, timedelta

from phonenumbers import parse, format_number, PhoneNumberFormat
from phonenumbers.phonenumberutil import NumberParseException
from rest_framework import serializers

from faucet.models import Account
from passcode.models import PassRequest


class NumberSerializer(serializers.Serializer):
    number = serializers.CharField()

    def validate_number(self, number):
        try:
            number = format_number(parse(number), PhoneNumberFormat.E164)
        except NumberParseException:
            raise serializers.ValidationError('Invalid number')

        if Account.objects.filter(number=number, is_created=True).exists():
            raise serializers.ValidationError(
                'Account with this phone already registered: %s' %
                Account.objects.get(number=number).name)

        return number


class PassRequestSerializer(NumberSerializer,
                            serializers.ModelSerializer):
    # FIXME Проверять на фронтенде
    # TODO Регулярка для имени аккаунта
    # account = serializers.RegexField('^([a-z1-5]){12}$')
    # account = serializers.CharField(max_length=12)

    # def validate_account(self, account):
    #     if eos.account_exists(account):
    #         raise serializers.ValidationError('Account already exists')

    #     return account

    def validate(self, data):
        # Отправить код можно только раз в 5 минут.
        active_time = datetime.now() - timedelta(minutes=5)

        if PassRequest.objects.filter(
                number=data['number'],
                created_at__gt=active_time).exists():

            raise serializers.ValidationError('SMS can be sent in 5 minutes')

        return data

    class Meta:
        model = PassRequest
        fields = 'number',


class PassRequestValidateSerializer(NumberSerializer):
    passcode = serializers.CharField()

    def validate(self, data):
        # Код активен в течении двух минут
        active_time = datetime.now() - timedelta(minutes=2)

        if not PassRequest.objects.filter(
            number=data['number'],
            code=data['passcode'],
            created_at__gt=active_time
        ).exists():
            raise serializers.ValidationError('Wrong sms code')
        else:
            return data
