from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     CreateAPIView, RetrieveUpdateAPIView,
                                     )

#custom permission
from meeting.api.permissions import IsOwner
from meeting.api.serializers import MeetingSerializer, MeetingUpdateCreateSerializer
from meeting.models import Meeting
from rest_framework.permissions import (
IsAuthenticated,
IsAdminUser,
)




class MeetingListAPIView(ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer



class MeetingCreateAPIView(CreateAPIView):
    queryset = Meeting.objects.all()
    # POST işlemi olduğu için yine aynı serializer ı kullandık.
    serializer_class = MeetingUpdateCreateSerializer
    permission_classes = [IsAuthenticated]




class MeetingDetailAPIView(RetrieveAPIView):
    queryset = Meeting.objects.all()
    #POST işlemi olduğu için yine aynı serializer ı kullandık.
    serializer_class = MeetingSerializer
    #slug a göre url kısmı yapılacak.
    lookup_field = 'slug'


class MeetingDestroyAPIView(DestroyAPIView):
    queryset = Meeting.objects.all()
    #POST işlemi olduğu için yine aynı serializer ı kullandık.
    serializer_class = MeetingSerializer
    #slug a göre url kısmı yapılacak.
    lookup_field = 'slug'
    permission_classes = [IsOwner]

class MeetingUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Meeting.objects.all()
    #POST işlemi olduğu için yine aynı serializer ı kullandık.
    serializer_class = MeetingUpdateCreateSerializer
    #slug a göre url kısmı yapılacak.
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)
