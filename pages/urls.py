from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact_submit, name="contact_submit"),
    path("online_shop/", views.online_shop, name="online_shop"),
    path("health_stack/", views.health_stack, name="health_stack"),
    path("classmanager/", views.classmanager, name="classmanager"),
    path("lapzone/", views.lapzone, name="lapzone"),
    path("gym/", views.gym, name="gym"),
    path("train_food/", views.train_food, name="train_food"),
    path("Hotel_room/", views.Hotel_room, name="Hotel_room"),
    path("job_portal/", views.job_portal, name="job_portal"),
    path("contact_view/", views.contact_view, name="contact_view"),
]
