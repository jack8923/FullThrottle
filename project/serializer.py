import logging

from rest_framework import serializers

from .models import Members, Activity_Periods


class ActivitySerializer(serializers.ModelSerializer):
    # member_name = serializers.CharField(source="member.real_name", read_only=True
    #                                        )

    class Meta:
        model = Activity_Periods
        fields = ("start_time", "end_time")


logger = logging.getLogger(__name__)


class MembersSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True,read_only=True)

    class Meta:
        model = Members
        fields = ("id", "real_name", "tz", "activity_periods")

