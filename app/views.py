from django.shortcuts import render
from django.http.response  import HttpResponse
from .generators import simulate_profit_loss
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from app.models import TradingView
import random 



def dashboard(request):
    data = simulate_profit_loss()
    return render(request, 'app/dashboard.html', {'data': data, 
                                                  'role': "Admin"
                                                  })


def home(request):
    return render(request, 'app/home.html')

def traderview(request):
    return render(request, 'app/user_dashboard.html')


User = get_user_model()

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            if user.role == 'admin':
                return redirect('admin_dashboard')  
            else:
                starting_amount = 100
                profit_loss = random.uniform(-50, 50)  
                final_amount = starting_amount + profit_loss
                
                user.profit_loss = profit_loss
                user.final_amount = final_amount
                user.save()

                TradingView.objects.create(
                    startoff_amount=starting_amount,
                    profit_loss=profit_loss,
                    final_amount=final_amount,
                    user=user
                )
                trading_view = TradingView.objects.filter(user=user)

                data = {
                     'trader': user,
                    'trading_view': trading_view
                }
                return render(request, 'app/user_dashboard.html', {"data": data})
        else:
            return HttpResponse('User does not exist')
        
    return render(request, 'home.html')
