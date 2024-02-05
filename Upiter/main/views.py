from django.shortcuts import render, redirect
from .utils import  get_alternative_assets
from django.conf import settings
from main.models import Users, DebitCard, CreditCard, PlatinumCard, Transfer, Transfers, ImageTransfers, Messenger
from .serializers import serialize_user_data, UserImage, SerializeTransfers, SerializeImages, SerlMessage
from django.views.decorators.csrf import requires_csrf_token
import json
# Create your views here.
def slider(request):
    delSession(request)
    usersess = request.session.get(settings.SESSION_USER, {})
    length = len(usersess)
    request.session.pop(settings.SESSION_PAGE, None)
    data = {
        "length": length,
    }
    return render(request, "main/slider.html", data)

def autoriz(request):
    delSession(request)
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
    if len(usersess) > 0:
        users = Users.objects.all()[:6]
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


    rate = get_alternative_assets()
    data ={
         "rate": rate, "length": length,
        "usersess": usersess, "debitcard": debitcard, "creditcard": creditcard, "platinumcard": platinumcard,
        "page": pages, "pagelen" : pagelen, "users": users,
    }
    return render(request, "main/upiter.html", data)


def history(request):
    delSession(request)
    usersess = request.session.get(settings.SESSION_USER, {})
    length = len(usersess)
    if(length) > 0:
        for el in usersess:
            sender1 = json.dumps(el['name'])
            sendersur1 = json.dumps(el['surname'])
            sender = el['name']
            sendersur = el['surname']
        images = json.dumps(SerializeImages(ImageTransfers.objects.all(), many = True).data)
        transfers = Transfers.objects.filter(Sender = sender, SenderSurname = sendersur) 
        histtransfer = json.dumps(SerializeTransfers(Transfers.objects.filter(Recipient = sender, RecipientSurname = sendersur), many =True).data)
        serialized = SerializeTransfers(transfers, many = True)
        transferss = json.dumps(serialized.data)
    data ={
        "usersess": usersess, "length": length, "transfers":transferss, "sender": sender1, "sendersur": sendersur1, "images": images, "histtransfer": histtransfer,
    }
    return render(request, "main/history.html",  data)

def pageTransaction(request):
    usersess = request.session.get(settings.SESSION_USER, {})
    length = len(usersess)

    data ={
        "usersess": usersess, "length": length,
    }
    return render(request, "main/transaction.html",  data)


@requires_csrf_token
def transfer(request):
    usersess = request.session.get(settings.SESSION_USER, {})
    choose_transfer = request.session.get(settings.SESSION_CHOOSE_TRANSFER, {})
    transferDebit =  transferCredit = transferPlatinum = selected_user = ""
    length_choose_transfer =len(choose_transfer)
    if len(choose_transfer) != 0:
        for el in choose_transfer:
            name = el['name']
            surname = el['surname']
            phone = el['phone']
        selected_user = Users.objects.filter(name = name, surname = surname, phone = phone).first()
        transferDebit = DebitCard.objects.filter(name = name, surname = surname, phone = phone).first()
        transferCredit = CreditCard.objects.filter(name = name, surname = surname, phone = phone).first()
        transferPlatinum = PlatinumCard.objects.filter(name = name, surname = surname, phone = phone).first()
    if transferPlatinum:pass
    else:
        transferPlatinum = 0
    length = len(usersess)
    debitcard = creditcard = platinumcard = ""
    ussers = ""
    if len(usersess) > 0:
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
    data ={
        "usersess": usersess, "length": length, "debitcard": debitcard, "creditcard": creditcard, "platinumcard": platinumcard,
        "ussers": ussers, "selected_user": selected_user, "transferCredit": transferCredit, "transferDebit": transferDebit, "transferPlatinum": transferPlatinum,
        "length_choose_transfer": length_choose_transfer,
    }
    return render(request, "main/transfer.html", data)


def messenger(request):
    delSession(request)
    choose_user = request.session.get(settings.MESSEGE_CHOOSE_USER, {})
    usersess = request.session.get(settings.SESSION_USER, {})
    length = len(usersess)
    userPhone = ""
    userName = ""
    choose_user_phone = ""
    message_send_user =""
    message_get_user =""
    phones = ""
    choose_user_phones = ""

    if len(usersess) > 0:
        serialized_users = json.dumps(UserImage(Users.objects.all(), many=True).data)
        for el in usersess:
            userPhone = json.dumps(el['numberphone'])
            userName = json.dumps(el['name'])
            phones = el['numberphone']
            print(phones)

    if len(choose_user) > 0:    
        for el in choose_user:
            choose_user_phone = json.dumps(el["phones"])
            choose_user_phones = el['phones']
            print(choose_user_phones)

    message_send_user = json.dumps(SerlMessage(Messenger.objects.filter(Sender = choose_user_phones, Recipient = phones ), many = True).data)
    message_get_user = json.dumps(SerlMessage(Messenger.objects.filter(Sender = phones, Recipient = choose_user_phones ), many = True ).data)

    data ={
        "usersess": usersess, "length": length, "serialized_users": serialized_users, "userName": userName, "userPhone": userPhone, "choose_user_phone": choose_user_phone,
        "message_send_user" : message_send_user, "message_get_user": message_get_user,
    }
    return render(request, "main/messenger.html", data)

def SetUsers(request):
    choose_user = request.session.get(settings.MESSEGE_CHOOSE_USER, {})

    if request.method == "POST":
        choose_user = request.session.pop(settings.MESSEGE_CHOOSE_USER, None)
        choose_user = []
        name = request.POST.get("userName-choose")
        phone = request.POST.get("userPhone-choose")

        choose_user.append({
            "name": name, "phones": phone
        })

        request.session[settings.MESSEGE_CHOOSE_USER] = choose_user
    return redirect("messenger")

def addMessage(request):
    choose_user = request.session.get(settings.MESSEGE_CHOOSE_USER, {})
    usersess = request.session.get(settings.SESSION_USER, {})
    if request.method == "POST":
        text = request.POST.get("text")
        date = request.POST.get("date")
        time = request.POST.get("time")

        for el in choose_user:
            recipient = el['phones']
        for user in usersess:
            sender = user['numberphone']
            message = Messenger(Sender=sender, Recipient=recipient, message=text, Date=date, Time=time)
            message.save()

    return redirect("messenger")

def exit(request):
    delSession(request)
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
    delSession(request)
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

def selectTransfer(request):
    choose_transfer = request.session.get(settings.SESSION_CHOOSE_TRANSFER, {})
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phone = request.POST.get("phone")

        choose_transfer = []
        choose_transfer.append({
            "name": name, "surname": surname, "phone": phone,
        })

        request.session[settings.SESSION_CHOOSE_TRANSFER] = choose_transfer

        return redirect("transfer")

def delSession(request):
    request.session.pop(settings.SESSION_CHOOSE_TRANSFER, None)

def transaction(request):
    usersess = request.session.get(settings.SESSION_USER, {})
    if request.method == "POST":
        sender = ""
        for el in usersess:
            sender = el['name']
            senderSurname = el['surname']
        recipient = request.POST.get("name")
        recipientSurname = request.POST.get("surname")
        whereFrom = request.POST.get("fromCard")
        where = request.POST.get("numberCard")
        if len(whereFrom)>19 or len(whereFrom) < 19: return redirect("transfer")
        date = request.POST.get("date")
        time = request.POST.get("time")
        summ = request.POST.get("summ")
        numberPhone = request.POST.get("numberPhone")
        CardNameOfDepozit = FoundNameCard(where)
        CardNameOffs = FoundNameCard(whereFrom)
        
        result1 = Payments(request, whereFrom, summ, CardNameOffs)
        if result1 != "negative" or result1 != None :
            Completion(where, summ, CardNameOfDepozit)

            data = {
                "where": where, "summ": summ, "whereFrom": whereFrom,
                "date":date, "time": time, "numberPhone": numberPhone, "CardNameOffs": CardNameOffs,
            }

            transfer = Transfers(Sender= sender, Recipient = recipient, WhereFrom = whereFrom, Where = where, Date = date, Time = time, Summ = summ, 
            CardNameOfDepozit = CardNameOfDepozit, CardNameOffs = CardNameOffs, SenderSurname = senderSurname, RecipientSurname = recipientSurname)

            transfer.save()
            delSession(request)
            return render(request, 'main/check.html', data)
        else:
            return redirect("transfer")


def FoundNameCard(element):
    CardDebit = DebitCard.objects.filter(numbercard = element).first()
    CardCredit = CreditCard.objects.filter(numbercard = element).first()
    CardPlatinum = PlatinumCard.objects.filter(numbercard = element).first()
    answer =""
    if CardDebit:
        answer = "Upiter Debits"
    elif CardCredit:
        answer = "Upiter Credits"
    elif CardPlatinum:
        answer = "Upiter Platinum"
    
    return answer

def Payments(request, whereFrom, summ, el1):
    result = ""
    if el1 == "Upiter Debits":
        PayFrom = DebitCard.objects.filter(numbercard = whereFrom).first()
        if float(PayFrom.Check) - float(summ) >= 0:
            PayFrom.Check = round(float(PayFrom.Check) - float(summ), 8)
            PayFrom.save()
        else:
            delSession(request)
            result = "negative"
    elif el1 == "Upiter Credits":
        PayFrom = CreditCard.objects.filter(numbercard = whereFrom).first()
        if float(PayFrom.Check) - float(summ) > float(PayFrom.Limit):
            PayFrom.Check = round(float(PayFrom.Check) - float(summ), 8)
            PayFrom.save()
        else:
            delSession(request)
            result = "negative"
    elif el1 == "Upiter Platinum":
        PayFrom = PlatinumCard.objects.filter(numbercard = whereFrom).first()
        if float(PayFrom.Check) - float(summ) > float(PayFrom.Limit):
            PayFrom.Check = round(float(PayFrom.Check) - float(summ), 8)
            PayFrom.save()
        else:
            delSession(request)
            result = "negative"
    return result


    
def Completion(where,summ ,el2):
    if el2 == "Upiter Debits":
        PayWhere = DebitCard.objects.filter(numbercard = where).first()
    elif el2 == "Upiter Credits":
        PayWhere = CreditCard.objects.filter(numbercard = where).first()
    elif el2 == "Upiter Platinum":
        PayWhere = PlatinumCard.objects.filter(numbercard = where).first()

    PayWhere.Check = float(PayWhere.Check) + float(summ)
    PayWhere.save()


