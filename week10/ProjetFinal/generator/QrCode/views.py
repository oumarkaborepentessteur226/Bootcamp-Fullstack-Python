from django.shortcuts import render
from qrcode import*

# Create your views here.market://details?id=org.example.foo
data=None


def demo(request):
    global data
    if request.method == "POST":
        data1 = request.POST['data1']

        data = data1
        img = make(data)
        img.save('QrCode/static/images/test.png')


    else:
        pass
    return render(request,'qr/base.html', {'data': data})


def tel(request):
    global data
    if request.method == "POST":
        data1 = request.POST['data1']

        data = data1
        img = make(data)
        img.save('QrCode/static/images/test.png')


    else:
        pass

    return render(request, 'qr/tel.html', {'data': data})

def sms(request):
    global data
    if request.method == "POST":
        data1 = request.POST['data1']

        data = data1
        img = make(data)
        img.save('QrCode/static/images/test.png')


    else:
        pass

    return render(request, 'qr/sms.html', {'data': data})


def email(request):
    global data
    if request.method == "POST":
        data1 = request.POST['data1']

        data = data1
        img = make(data)
        img.save('QrCode/static/images/test.png')


    else:
        pass

    return render(request, 'qr/email.html', {'data': data})


def wiffi(request):
    global data
    if request.method == "POST":
        data1 = request.POST['data1']

        data = data1
        img = make(data)
        img.save('QrCode/static/images/test.png')


    else:
        pass

    return render(request, 'qr/wiffi.html', {'data': data})

def accueil(request):

    return render(request, 'qr/acceuil.html')

"""
# Address
mailto:someone@yoursite.com


# NYC Directory assistance
tel:+12125551212

#carte 
BIZCARD:N:Sean;
X:Owen;
T:Software Engineer;
C:Google;
A:76 9th Avenue, New York, NY 10011;
B:+12125551212;
E:srowen@google.com;;

#appeler et ajouter
BIZCARD:NB:+12125551212;
BIZCARD:NB:E:srowen@google.com


# Send an SMS/MMS to a number
sms:+18005551212

# Send an SMS/MMS to a number with pre-filled message.
sms:+18005551212:This%20is%20my%20text%20ton modia.

#calandar
BEGIN:VEVENT
SUMMARY:Summer+Vacation!
DTSTART:20180601T070000Z
DTEND:20180831T070000Z
END:VEVENT


#wiffi
WIFI:T:WPA;
S:mynetwork;
P:mypass;;

#googleplay
market://details?id=org.example.foo


"""