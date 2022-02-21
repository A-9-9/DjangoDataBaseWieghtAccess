
from django.contrib import admin
from django.urls import path, include
import stocks
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/', include('stocks.urls'))
]
