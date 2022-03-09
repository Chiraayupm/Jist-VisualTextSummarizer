from django.shortcuts import render, redirect
from news_graph.trying import ml_summmarizer

def summarization(request):
    if request.method == "POST":
        paratxt = request.POST["paratxt"]

        data_edges, data_nodes = ml_summmarizer(paratxt, "")
        print(data_edges, data_nodes)

    return render(request, 'summarization.html')