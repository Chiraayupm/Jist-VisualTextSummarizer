from django.urls import path
from .views import main, index, summarization

urlpatterns = [
    # path('', main.main, name=""),
    path('', index.index, name="index"),
    path('summarization/', summarization.summarization, name="summarization"),
    path('summarizationpdf/', summarization.summarize_pdf, name="summarizationpdf"),
]