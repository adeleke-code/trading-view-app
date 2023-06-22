from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid




class User(AbstractBaseUser):


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    
    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"



class TradingView(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    startoff_amount = models.IntegerField()
    profit_loss = models.IntegerField()
    final_amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "tradingview"
        verbose_name = "TradingView"
        verbose_name_plural = "TradingViews"

    def __str__(self):
        return self.user.email