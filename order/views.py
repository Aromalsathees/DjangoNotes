from django.shortcuts import render
from django.conf import setting
from .models import Payment

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def create_order(request):

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    amount = 500 
    amount_paise = amount * 100   

    razorpay_order = client.order.create({
        "amount":amount_paise,
        "currency":"INR",
        "payment_capture":"1"
    })

    # save order in DB
    payment = Payment.objects.create(
        order_id = razorpay_order['id']
        amount=amount_paise,
        status="created"
    )

    context = {
        "payment":razorpay_order,
        "razorpay_key":settings.RAZORPAY_KEY_ID
    }
    return render(request, 'payment.html', context)



@csrf_exempt
def verfiy_payment(request):
     
     if request.method == 'POST':
          data = json.loads(request.body)

          client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

          params_dict = {
               "razorpay_order_id": data['razorpay_order_id'],
               "razorpay_payment_id":data['razorpay_payment_id'],
               "razorpay_signature":data['razorpay_signature']
          }

          try:
               client.utilty.verify_payment_signature(params_dict)

               payment = Payment.objects.get(order_id=data['razorpay_order_id'])
               payment.payment_id = data['razorpay_payment_id']
               payment.signature = data['razorpay_signature']
               payment.status = 'success'
               payment.save()

               return JsonResponse({'message':'payment successfull'})
          except:
               return JsonResponse({'message':'payment failed'})
