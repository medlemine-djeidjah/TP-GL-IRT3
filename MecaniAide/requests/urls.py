from django.urls import path
from .views import submit_request,service_provider_requests, track_request, delete_request, get_request_details,assistance_stats

urlpatterns = [
    path('submit-request/', submit_request, name='submit_request'),
    path('service-provider/requests/', service_provider_requests, name='service_provider_requests'),
    path('service-provider/request/<int:request_id>/', track_request, name='track_request'),
    path('service-provider/request/<int:request_id>/delete/', delete_request, name='delete_request'),
    path('request_details/<int:request_id>/', get_request_details, name='get_request_details'),
    path('assistance-stats/', assistance_stats, name='assistance_stats'),
]
