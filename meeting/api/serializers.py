from rest_framework import serializers
from meeting.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = "__all__"

#yeni oluşumunda ve ya update esnasında created date modified date leri api ye sunmamak için düzenleme yapıldı.
class MeetingUpdateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ("user","title","subject","meeting_date","meeting_start_time","meeting_end_time","meeting_members","draft","meeting_image","modified_by")
