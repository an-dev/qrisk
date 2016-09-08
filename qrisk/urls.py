from django.conf.urls import url
# from django.contrib import admin
from qrisk.calculator.views import QInfoDetail

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^calculate/', QInfoDetail.as_view(), name='calculate'),
]
