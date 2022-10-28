from django.shortcuts import render
import pdfkit
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .forms import Fprofile
from .models import Profile
from django.template.loader import get_template


# Create your views here.
def index(request):
    form=Fprofile()
    if request.method == 'POST':
        form = Fprofile(request.POST , request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            new=Profile.objects.create(**form.cleaned_data)
            new.save()
            return redirect('verification')


    else:
        form=Fprofile()
    return render(request, 'pdf/image.html',{'form':form})

"""def formulaire(request):
    if request.method == "POST":
        image= request.POST.get('image')
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        competence = request.POST.get('competence')
        langue = request.POST.get('langue')
        interet = request.POST.get('interet')
        profile = request.POST.get('profile')
        experience = request.POST.get('experience')
        education = request.POST.get('education')
        projet = request.POST.get('projet')
        qualite= request.POST.get('qualite')


        donnees = Profile.objects.create(name=name, username=username, email=email,
                          phone=phone, address=address,
                          competance=competence, langue=langue,
                          interet=interet,profile=profile,
                          experience=experience,education=education,
                          Projet=projet,qualite=qualite,image=image)
        donnees.save()
        return redirect('verification')
    return render(request, 'pdf/form.html')"""

def verification(request):
    profiles = Profile.objects.all()[:1]
    for profile in profiles:
        image=profile.image
        name=profile.name
        username = profile.username
        phone=profile.phone
        email =profile.email
        address =profile.address
        competance = profile.competance
        langue = profile.langue
        interet = profile.interet
        experience = profile.experience

        education = profile.education
        project = profile.Projet

    return render(request, "pdf/verification.html", {'image':image,'address':address, 'name':name, 'email':email, 'phone':phone, 'competance':competance, 'interet':interet, 'langue':langue, 'experience':experience, 'username':username, 'education': education, 'project':project})

def generer(request, id):

    profile = Profile.objects.get(pk=id)
    image = Profile.image
    name=profile.name
    username = profile.username
    phone=profile.phone
    email =profile.email
    address =profile.address
    competance = profile.competance
    langue = profile.langue
    interet = profile.interet
    experience = profile.experience
    education = profile.education
    project = profile.Projet

    template = get_template('pdf/generator.html')
    context = {'image':image,'address':address, 'name':name, 'email':email, 'phone':phone, 'competance':competance, 'interet':interet, 'langue':langue, 'experience':experience, 'username':username, 'education': education, 'project':project}
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)

    reponse = HttpResponse(pdf, content_type='application/pdf')
    reponse['Content-Disposition']="attachement"
    return reponse

def download(request):
    profile = Profile.objects.all()
    return render(request, 'pdf/download.html', {'profile':profile})



