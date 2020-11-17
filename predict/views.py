from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import simplejson as json

BASE_URL = 'https://covidtest.dhakalaashish.com.np'

# Create your views here.
def PostRequest(request):
    message = 'Upload your X-Ray Here'
    if request.method == 'POST':

        imageuploadURL = (f"{BASE_URL}/api/imageupload/")
        file = {'image': request.FILES['image']}
        response = requests.post(imageuploadURL, files=file)
        print(response.text)
        data = json.loads(response.text)
        imgUrl = data['image']

        predictURL = (f"{BASE_URL}/api/predict/")
        imageURL = (BASE_URL+imgUrl)
        data = {'image':imageURL}
        response = requests.post(predictURL, data=data)
        print(response.text)

        data = json.loads(response.text)
        prediction = (f"You have {data['prediction']}. {data['message']}")
        res = data['prediction']
        messageApi = data['message']
    else:
        res = ''
        messageApi=''
        imageURL =''

    context = {'message':message, 'res':res, 'messageApi':messageApi, 'image':imageURL}
    return render(request, 'index1.html', context)
