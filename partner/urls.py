from django.contrib import admin
from django.urls import path, include
from taxi import views
from api.urls import AccountAPIView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('taxi/', include('taxi.urls')),
    path('api/', include('api.urls')),
    path('api/account/', AccountAPIView.as_view()),

]
