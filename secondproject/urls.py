from django.contrib import admin
from django.urls import path
import lotto.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lotto.views.home, name="home"),
    path('result/', lotto.views.result, name="result"), 
]
