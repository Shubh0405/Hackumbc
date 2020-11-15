from django.urls import path
from eportal import views

app_name = 'eportal'

urlpatterns = [
    path('',views.index,name="home"),
    path('ocr/',views.ocr_page,name="ocr_page"),
    path('ocr_output/',views.ocr_output,name="ocr_output"),
    path('synthesizer/',views.synthesizer,name="synthesizer"),
]
