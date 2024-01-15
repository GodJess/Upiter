from django.shortcuts import render, redirect
from .utils import get_exchange_rates, get_alternative_assets
from django.conf import settings
from main.models import Users, DebitCard, CreditCard, PlatinumCard
from .serializers import serialize_user_data, UserImage
import json
# Create your views here.
def slider(request):
    usersess = request.session.get(settings.SESSION_USER, {})
    length = len(usersess)
    request.session.pop(settings.SESSION_PAGE, None)
    data = {
        "length": length,
    }
    return render(request, "main/slider.html", data)

def autoriz(request):
    error =""
    if request.method == "POST":
        usersess = request.session.get(settings.SESSION_USER, {})
        request.session.pop(settings.SESSION_USER, None)
        numberphone = request.POST.get("numberphone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if len(str(numberphone)) > 0 and len(str(email)) > 0 and int(len(str(password))) >= 8:

            auth = Users.objects.filter( phone = numberphone, email = email, password = password).first()
            if auth:
                if auth.active:
                # serialize_user_data = serialize_user_data(auth)
                    photo = auth.photo.url
                    usersess = []
                    usersess.append({
                        "name": auth.name, "surname": auth.surname, "numberphone": auth.phone, "email": auth.email, 
                        "password": auth.password, "photo":  photo
                    })
                    request.session.pop(settings.SESSION_PAGE, None)
                    request.session[settings.SESSION_USER] = usersess
                    return redirect("upiter")
                else:
                    error = "ваш аккаунт еще не активирован"
            else:
                error = "данные введены не верно"
        else:
            error = "Некорректная длина"
    data = {
        "error" : error,
    }
    return render(request, "main/autoriz.html", data)

def upiter(request):
    usersess = request.session.get(settings.SESSION_USER, {})
    page = request.session.get(settings.SESSION_PAGE, {})
    pages =""
    users = ""
    pagelen = len(page)
    if len(page) > 0:
        for el in page:
            pages = el['page']
    length = len(usersess)
    debitcard = ""
    creditcard = ""
    platinumcard = "" 
    ussers = ""
    if len(usersess) > 0:
        users = Users.objects.all()[:7]
        serialized_users = UserImage(Users.objects.all(), many=True)
        ussers = json.dumps(serialized_users.data)
        for el in usersess:
            name = el['name']
            surname = el['surname']
            email = el['email']
        debitcard = DebitCard.objects.filter(name = name, surname = surname, email = email).first()
        creditcard = CreditCard.objects.filter(name = name, surname = surname, email = email).first()
        platinumcard = PlatinumCard.objects.filter(name = name, surname = surname, email = email).first()
    if platinumcard:pass
    else:
        platinumcard = 0

    rates = get_exchange_rates("d0b062b411bc5980a45f2c5a16e2d6fc")
    rate = get_alternative_assets()
    data ={
        "rates": rates, "rate": rate, "length": length,
        "usersess": usersess, "debitcard": debitcard, "creditcard": creditcard, "platinumcard": platinumcard,
        "page": pages, "pagelen" : pagelen, "users": users, "ussers": ussers,
    }
    return render(request, "main/upiter.html", data)

def exit(request):
    usersess = request.session.get(settings.SESSION_USER, {})
    if request.method == "POST":
        request.session.pop(settings.SESSION_USER, None)
    return redirect("upiter")

def loadImage(request):
    if request.method == "POST":
        usersess = request.session.get(settings.SESSION_USER, {})
        newImage = request.FILES.get("newImage")
        
        for el in usersess:
            phone = el['numberphone']
            name = el['name']
            surname = el['surname']
            
        user = Users.objects.filter(name = name, surname = surname, phone = phone).first()
        if user:

            user.photo.save(newImage.name, newImage)
            user.save()

            for el in usersess:
                    el["photo"] = user.photo.url
        request.session[settings.SESSION_USER] = usersess

    return redirect("upiter")

def setpage(request, name):
    if name == "home":
        request.session.pop(settings.SESSION_PAGE, None)
    else:
        page = request.session.get(settings.SESSION_PAGE, {})
        page = []
        page.append({
            "page": name
        })
        request.session[settings.SESSION_PAGE] = page 
        
    return redirect("upiter")