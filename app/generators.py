import random
from django.contrib.auth import get_user_model
from app.models import TradingView

User = get_user_model()

def simulate_profit_loss():
    traders = User.objects.filter(role='trader')

    data = []
    for trader in traders:
        starting_amount = 100 
        profit_loss = random.uniform(-50, 50)  
        final_amount = starting_amount + profit_loss
        trader.profit_loss = profit_loss
        trader.final_amount = final_amount
        trader.save()

        trading_view = TradingView.objects.create(
            startoff_amount=starting_amount,
            profit_loss=profit_loss,
            final_amount=final_amount,
            user=trader
        )

        data.append({
            'trader': trader,
            'trading_view': trading_view
        })

    return data
