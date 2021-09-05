import requests
import json

BASE_URL = 'https://covidtest.dhakalaashish.com.np'


def predict(imgUrl):
    predictURL = (f"{BASE_URL}/api/predict/")
    fullImgUrl = (BASE_URL+imgUrl)
    data = {'image':fullImgUrl}
    response = requests.post(predictURL, data=data)
    print(response.text)

    data = json.loads(response.text)
    print(data['prediction'])
    r = data['prediction']

    if r == "COVID 19":
        print("0")
    elif r == "Viral":
        print("1")
    else:
        print("2")


def imgUpload (filename):
    imageuploadURL = (f"{BASE_URL}/api/imageupload/")
    img = {'image': open(filename, 'rb')}
    response = requests.post(imageuploadURL, files=img)
    print(response.text)
    imgUrl = response.text["image"]
    print(imgUrl)
    predict(imgUrl)


# filename = '/Users/anony/Downloads/pneumonia.jpg'
# imgUpload(filename)
# predict('/media/images/pneumonia_t7mhrc1.jpg')



# Template("{{ imgUpload(filename) }}").render(imgUpload=imgUpload)
