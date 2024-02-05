from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField("User Name", max_length = 100)
    surname = models.CharField("User lname", max_length = 100)
    phone = models.CharField("User phone", max_length = 100)
    email = models.EmailField(unique=True)
    password = models.CharField("User password", max_length = 100)
    photo = models.ImageField(upload_to="images/")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class DebitCard(models.Model):
    CardName = models.CharField("Card Name", max_length = 100)
    name = models.CharField("User Name", max_length = 100)
    surname = models.CharField("User lname", max_length = 100)
    phone = models.CharField("User phone", max_length = 100)
    email = models.EmailField(unique=True)
    password = models.CharField("Card password", max_length = 4)
    numbercard = models.CharField("Number of Card", max_length = 19)
    Check = models.CharField("Checking account", max_length = 100)
    paymentSystem = models.CharField("Payment system", max_length = 100)
    ImagePaymentSys = models.ImageField(upload_to = "images/")
    Validity = models.DateField("Date Validity")
    CashBack = models.CharField("Summ of cash back", max_length = 100)
    CashbackPercentage = models.CharField("Precent of cash back", max_length = 100)
    ImageCB = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Дебетовая карта"
        verbose_name_plural = "Дебетовые карты"

class CreditCard(models.Model):
    CardName = models.CharField("Card Name", max_length = 100)
    name = models.CharField("User Name", max_length = 100)
    surname = models.CharField("User lname", max_length = 100)
    phone = models.CharField("User phone", max_length = 100)
    email = models.EmailField(unique=True)
    password = models.CharField("Card password", max_length = 4)
    numbercard = models.CharField("Number of Card", max_length = 19)
    Check = models.CharField("Checking account", max_length = 100)
    Limit = models.CharField("Limit", max_length = 100)
    paymentSystem = models.CharField("Payment system", max_length = 100)
    ImagePaymentSys = models.ImageField(upload_to = "images/")
    Validity = models.DateField("Date Validity" )
    CashBack = models.CharField("Summ of cash back", max_length = 100)
    CashbackPercentage = models.CharField("Precent of cash back", max_length = 100)
    ImageCB = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Кредитная карта"
        verbose_name_plural = "Кредитные карты"

class PlatinumCard(models.Model):
    CardName = models.CharField("Card Name", max_length = 100)
    name = models.CharField("User Name", max_length = 100)
    surname = models.CharField("User lname", max_length = 100)
    phone = models.CharField("User phone", max_length = 100)
    email = models.EmailField(unique=True)
    password = models.CharField("Card password", max_length = 4)
    numbercard = models.CharField("Number of Card", max_length = 19)
    Check = models.CharField("Checking account", max_length = 100)
    Limit = models.CharField("Limit", max_length = 100)
    paymentSystem = models.CharField("Payment system", max_length = 100)
    ImagePaymentSys = models.ImageField(upload_to = "images/")
    Validity = models.DateField("Date Validity")
    CashBack = models.CharField("Summ of cash back", max_length = 100)
    CashbackPercentage = models.CharField("Precent of cash back", max_length = 100) 
    ImageCB = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Платиновая карта"
        verbose_name_plural = "Платиновые карты"

class Transfer(models.Model):
    Sender = models.CharField("Отправитель", max_length = 100)
    Recipient = models.CharField("Получатель", max_length = 100)
    WhereFrom = models.CharField("Счет списания", max_length = 100)
    Where = models.CharField("Счет пополнения", max_length = 100)
    Date = models.DateField("Дата отправки")
    Time = models.TimeField("Время отправки")
    Summ = models.CharField("Сумма транзакции", max_length = 100)
    CardNameOfDepozit = models.CharField("Название карты пополнения", max_length = 100)
    CardNameOffs = models.CharField("Название карты списания", max_length = 100)

    def __str__(self):
        return self.Sender
    
    class Meta: 
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"

class Transfers(models.Model):
    Sender = models.CharField("Отправитель", max_length = 100)
    Recipient = models.CharField("Получатель", max_length = 100)
    WhereFrom = models.CharField("Счет списания", max_length = 100)
    Where = models.CharField("Счет пополнения", max_length = 100)
    Date = models.DateField("Дата отправки")
    Time = models.TimeField("Время отправки")
    Summ = models.CharField("Сумма транзакции", max_length = 100)
    CardNameOfDepozit = models.CharField("Название карты пополнения", max_length = 100)
    CardNameOffs = models.CharField("Название карты списания", max_length = 100)
    SenderSurname = models.CharField("Отправитель_фамилия", max_length = 100)
    RecipientSurname = models.CharField("Получатель_фамилия", max_length = 100)
    
    def __str__(self):
        return self.Sender
    
    class Meta: 
        verbose_name = "Перевод"
        verbose_name_plural = "Транзакции"

class ImageTransfers(models.Model):
        ImageUp = models.ImageField(upload_to = "images/")
        ImageDown = models.ImageField(upload_to = "images/")
    

        class Meta: 
            verbose_name = "Картинки"
            verbose_name_plural = "Картинки"

class Messenger(models.Model):
    Sender = models.CharField("Отправитель", max_length = 100)
    Recipient = models.CharField("Получатель", max_length = 100)
    message = models.TextField("Текст сообщения", max_length = 1000)
    Date = models.DateField("Дата отправки")
    Time = models.TimeField("Время отправки")

    def __str__(self):
        return self.Sender
    
    class Meta: 
        verbose_name = "Сообщения"
        verbose_name_plural = "Сообщение"
