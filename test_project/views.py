from django.http import HttpResponse
import pandas as pd
import PyPDF2 as pdf2

df = pd.read_csv("./data/m.csv")

df1 = df.to_json()

print(df1)

def home(request):
    return HttpResponse(df1)

def user(request):
    return HttpResponse("Hi there! python")

def readFile(request):
    with open("index.py", "r") as f:
            return HttpResponse(f)