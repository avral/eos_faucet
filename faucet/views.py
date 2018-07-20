import json

from rest_framework.views import Response, APIView
from rest_framework.permissions import AllowAny

from faucet.models import Account
from faucet.serializers import AccountCreateSerializer
from faucet.eos import create_account


class AccountView(APIView):
    permission_classes = AllowAny,

    def post(self, request):
        slz = AccountCreateSerializer(data=request.data)

        if slz.is_valid(raise_exception=True):
            data = slz.validated_data

            tx_result = create_account(
                data['account'],
                data['owner_pub'],
                data['active_pub']
            )

            if 'transaction' in tx_result:
                Account.objects.update_or_create(
                    name=data['account'],
                    number=data['number'],
                    is_created=True
                )
            else:
                Account.objects.update_or_create(
                    name=data['account'],
                    number=data['number'],
                    err_msg=json.dumps(tx_result)
                )

        return Response(tx_result)
