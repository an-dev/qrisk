from rest_framework import serializers

from qrisk.calculator.models import QUser, QUserInfo


class QUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = QUser


class QInfoSerializer(serializers.ModelSerializer):

    user = QUserSerializer(many=False, read_only=False)

    class Meta:
        model = QUserInfo
        fields = ('user', 'smoking_status', 'diabetes_status', 'heart_attacked_relative',
                  'kidney_disease', 'atrial_fibrillation', 'blood_pressure_treat',
                  'rheumatoid_arthritis', 'cholesterol_hdl_ratio', 'blood_pressure',
                  'height', 'weight')

    def create(self, validated_data):
        quser_data = validated_data.pop('user')
        QUser.objects.create(**quser_data)
        quser_info = QUserInfo.objects.create(**validated_data)
        return quser_info
