from qrisk.calculator.models import QUserInfo, QUser
from qrisk.calculator.serializers import QInfoSerializer
from qrisk.calculator.utils import calculate


from django.db import transaction

from rest_framework import generics, status
from rest_framework.response import Response


class QInfoDetail(generics.ListCreateAPIView):

    serializer_class = QInfoSerializer
    queryset = QUserInfo.objects.all()

    def post(self, request, *args, **kwargs):

        try:
            with transaction.atomic():
                resp = super(QInfoDetail, self).post(request, args, kwargs)
                quser = QUser.objects.last()
                # Calculate risk and then create object or viceversa?
                if resp.status_code == 201:
                    qrisk = calculate(quser)
                    return Response({
                        'qrisk': qrisk}, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'detail': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

