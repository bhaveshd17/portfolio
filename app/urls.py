from django.urls import path
from .views import home_view, send_msg_email

urlpatterns = [
    path('', home_view, name='home'),
    path('send_msg_email/', send_msg_email, name='send_msg_email'),
]