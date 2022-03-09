from django.http import HttpResponse
from django.shortcuts import render, redirect

def main(request):
    return HttpResponse({"hello"})