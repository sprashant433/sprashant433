from django.shortcuts import render
import requests,json
import google.auth.transport.requests
import google.oauth2.id_token
import urllib
import pathlib
import os
from looker.models import Topic,WebPage,AccessRecord
from looker.forms import FormName
from django.http import HttpResponse
from looker.forms import NewUserForm

def index(request):
    cred = os.path.join(pathlib.Path(__file__).parent.parent.parent.resolve(),'tgs-internal-saige-sandbox-001-fa1382577494.json')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =cred
    url = "https://us-central1-tgs-internal-saige-sandbox-001.cloudfunctions.net/looker_create_sso_embed_url"
    req = urllib.request.Request(url)
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)

    payload = json.dumps({
    "url": "/embed/dashboards/241"
    })
    headers = {
    'Authorization': f'Bearer {id_token}',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    embedlink = json.loads(response.text)
    
    return render(request,'index.html',context=embedlink)

def mainfun(request):
    webpages_list = AccessRecord.objects.order_by('date')
    mydic = {'access_records': webpages_list}
    return render(request,'main.html',context=mydic)

def form_content(request):
    form = FormName()
    if request.method=='POST':
        form = FormName(request.POST)
        
        if form.is_valid():
            print("Name" + form.cleaned_data['name'])
    mydic = {'form': form}
    return render(request,'form.html',mydic)

def test_fun(request):
    return HttpResponse("{'hii': 'prashant'}")

def users(request):
    form = NewUserForm()

    if request.method=='POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR in FORM")
    return render(request,'modelform.html',{'form':form})


