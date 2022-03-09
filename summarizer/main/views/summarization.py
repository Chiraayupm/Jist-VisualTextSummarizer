from django.shortcuts import render, redirect

def summarization(request):
    return render(request, 'summarization.html')