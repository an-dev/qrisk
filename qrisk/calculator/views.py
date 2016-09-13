from qrisk.calculator.models import QUserInfo, QUser
from qrisk.calculator.serializers import QInfoSerializer
from qrisk.calculator.utils import calculate


from django.db import transaction

from rest_framework import generics


class QInfoDetail(generics.ListCreateAPIView):

    serializer_class = QInfoSerializer
    queryset = QUserInfo.objects.all()

    def post(self, request, *args, **kwargs):

        with transaction.atomic():
            resp = super(QInfoDetail, self).post(request, args, kwargs)
            quser = QUser.objects.last()
            # Calculate risk and then create object or viceversa?
            if resp.status_code == 201:
                result = calculate(quser)

        return result

