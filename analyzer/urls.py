# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sentiment_analysis, name='sentiment_analysis'),
    path('translate/', views.translate_view, name='translate'),
    path('neutralize_sentiment/', views.neutralize_sentiment, name='neutralize_sentiment'),
]
