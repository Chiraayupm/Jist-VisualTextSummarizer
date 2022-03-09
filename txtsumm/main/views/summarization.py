from math import remainder
from django.shortcuts import render, redirect
from news_graph.trying import ml_summmarizer
from django.http import JsonResponse
from ..models import *

def summarization(request):
    if request.method == "POST":
        paratxt = request.POST["paratxt"]

        data_edges, data_nodes = ml_summmarizer(paratxt, "")

        new_data_edges = []
        new_data_nodes = []
        for data_edge in data_edges:
            new_data_edges.append({"key":data_edge["id"], "text":data_edge["label"]})
        
        for data_node in data_nodes:
            new_data_nodes.append({"from":data_node["from"], "to":data_node["to"]})

        # print(data_edges, data_nodes)
        print("newww")
        print(new_data_edges)
        print("***")
        print(new_data_nodes)

        context = {
            "new_data_edges":new_data_edges,
            "new_data_nodes":new_data_nodes
        }
        # return JsonResponse(context)
        return render(request, 'summarization.html', context)

    return render(request, 'summarization.html')

def summarize_pdf(request):
    if request.method == "POST":
        para_pdf = request.FILES.get("parapdf")
        print(para_pdf)
        para_pdf = ParaPdf.objects.create(pdf_file=para_pdf)
        print(para_pdf.pdf_file.url)
        data_edges, data_nodes = ml_summmarizer("", para_pdf.pdf_file.url)
    return render(request, 'summarization.html')