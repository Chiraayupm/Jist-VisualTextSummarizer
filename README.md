# Jist-VisualTextSummarizer
<br />

<p align="center">
    <img src="summarizer/static/assets/logo.png" width="140" height="140"/>
</p>

<h2 align="center">JIST | A Visual Text Summarization Tool</h2>
<br />

<p align="justify">
    A Visual text Summarization tool as a web application to summarize long paragraphs and also create a mind map of keywords for visual summarization of the same.
</p>

### Team 3: ic3

### Members
- Chiraayu Meghnani
- Parth Cheulkar
- Varun Mamtora
- Tanya Chandnani

### Problem Statement
VISUAL TEXT SUMMARIZATION | In today's world people are not interested in reading long articles or research papers hence, they use summarization tools, now there are many text summarization tools available in the market which are free to use as well as provide accurate summarizations.

### Approach
- Designing a Webapplication with minimilistic and sleek UI
- Allow user to add Raw text information or a pdf conatining the same
- Provide the result as a summarization of the long paragraph
- Also provide a visual graph sturcture of the important keywords to create your own mind map

## Features 

- Simplistic and Sleek UI 
- Summarisation of long paragraphs using BERT (Bidirectional Encoder Representations from Transformers), bert-extactive-summarizer
- Visual Representation of the keywords in the form of Flow Graphs using Relation Extraction

## Tech-stack

- HTML, CSS, Bootstrap
- Django rest framework
- SpaCy, Tensorflow

## Motivation?

- To build something that is relevant as everyone wouldn't want to read multiple long paragraphs and would like to skim through the basic plot
- Also as most people would rather prefer a visual summary of the long paragraph to implement such a feature
- To work with NLP

## How it produces the results for Visual Summarization
- For the basic summarization on long paragraphs [bert-extractive-summarizer](https://pypi.org/project/bert-extractive-summarizer/) library was used to produce accurate results.
- For the visual summarization use of Entity extraction along with text rank algorithm and [Relation Extraction](https://towardsdatascience.com/how-to-train-a-joint-entities-and-relation-extraction-classifier-using-bert-transformer-with-spacy-49eb08d91b5c) was used as reference to the open sourced github code which was tweaked for personal usecase [here](https://github.com/BrambleXu/news-graph)

## How it looks....
<p align="center">
    <img src="summarizer/static/assets/ps1.png" width="750" height="350"/>
</p>
<br/>
<p align="center">
    <img src="summarizer/static/assets/ps2.png" width="750" height="350"/>
</p>
<br/>
<p align="center">
    <img src="summarizer/static/assets/ps3.png" width="750" height="350"/>
</p>
<br/>
<p align="center">
    <img src="summarizer/static/assets/ps4.png" width="750" height="350"/>
</p>
<br/>
<p align="center">
    <img src="summarizer/static/assets/ps5.png" width="750" height="350"/>
</p>
<br/>

## Authors

- **Chiraayu Meghnani**
    - [LinkedIn](http://www.linkedin.com/in/chiraayu-pravin) | [Gmail](mailto:chiraayupm@gmail.com) 
- **Parth Cheulkar**
    - [Linkedin](https://linkedin.com/in/parthcheulkar/) | [Gmail](mailto:pscheulkar12@gmail.com) | [Twitter](https://twitter.com/Parth_Vader__)
- **Varun Mamtora**
    - [LinkedIn](https://www.linkedin.com/in/varun-mamtora-0b725b171/) | [Gmail](mailto:varunmamtora@gmail.com) | [Twitter](https://twitter.com/MamtoraVarun) | [Angel.co](https://angel.co/u/varun-mamtora)
- **Tanya Chandnani**
    - [Linkedin](https://www.linkedin.com/in/tanya-chandnani) | [Gmail](mailto:tanya.r.chandnani@gmail.com) | [Twitter](https://twitter.com/tanya_chandnani)
