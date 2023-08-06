from django.urls import path, re_path
from django.views.generic import TemplateView

from NEMO_user_details import views

urlpatterns = [
	# Override modify user page to add user details fields
    re_path(r"^user/(?P<user_id>\d+|new)/", views.create_or_modify_user_and_details, name='create_or_modify_user_and_details'),
]