

from django.urls import path

from meeting.api.views import (
    MeetingListAPIView,
    MeetingDetailAPIView,
    MeetingUpdateAPIView,
    MeetingDestroyAPIView,
    MeetingCreateAPIView,
                            )

urlpatterns = [
    #api/meeting/
    path('list/',MeetingListAPIView.as_view(),name='api-list'),

    path('create/',MeetingCreateAPIView.as_view(),name='api-create'),
    path('detail/<slug>',MeetingDetailAPIView.as_view(),name='api-detail'),
    path('update/<slug>',MeetingUpdateAPIView.as_view(),name='api-update'),
    path('delete/<slug>',MeetingDestroyAPIView.as_view(),name='api-delete')
]
