from django.conf.urls import url
from . import views
print "*"*100
urlpatterns= [
    url(r'^$', views.book_index)
]
