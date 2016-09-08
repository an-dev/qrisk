from qrisk.calculator.models import QUserInfo
from qrisk.calculator.serializers import QInfoSerializer

from rest_framework import generics


class QInfoDetail(generics.ListCreateAPIView):

    serializer_class = QInfoSerializer
    queryset = QUserInfo.objects.all()

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        return super(QInfoDetail, self).post(request, args, kwargs)
