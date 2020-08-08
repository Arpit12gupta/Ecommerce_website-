from django.shortcuts import render, HttpResponse, redirect
from math import ceil
from .models import (
    Product,
    Category,
    Contact,
    Orders,
    User,
    OrderUpdate,
    PayWithRazorpay,
    Razorpay,
)
import razorpay
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
import json
# from django.http import HttpResponse
# from django.contrib.auth.models import User

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n=len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides), 'products': products}
    # allProds = [[products, range(1,nSlides), nSlides],
    #             [products, range(1,nSlides), nSlides]]
    allProds = []
    catprods = Product.objects.values('product_category', 'Product_id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        n=len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def productView(request, Product_id):

    product = Product.objects.filter(Product_id=Product_id)
    print(product)

    return render(request, 'shop/prodView.html', {'product':product[0]})

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        # subject = request.POST.get('subject','')
        desc = request.POST.get('desc', '')
        # created_at = request.POST.get('created_at','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True 
        name = contact.name
        return render(request, 'shop/contact.html', {'thank':thank, 'name': name})

    return render(request, 'shop/contact.html')

def checkout(request):
    if request.method=="POST":
        
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        currency = request.POST.get('currency')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        # items_json = request.GET.get('itemsJson', '')
        # name = request.GET.get('name', '')
        # amount = request.GET.get('amount', '')
        # currency = request.GET.get('currency')
        # email = request.GET.get('email', '')
        # address = request.GET.get('address1', '') + " " + request.POST.get('address2', '')
        # city = request.GET.get('city', '')
        # state = request.GET.get('state', '')
        # zip_code = request.GET.get('zip_code', '')
        # phone = request.GET.get('phone', '')
        print(type(amount))
        print('------------------',amount)
        # print(int(amount))
        # JUST CHANGE FOR TESTING
        data={
            "amount":int(amount)*100,
            "currency":"INR",
            "payment_capture":1
        }
        # data={
            
        #     "payment_capture":1
        # }
        client = razorpay.Client(auth=("rzp_test_dgzzcZxUBrkJSW", "XOWQ750mgHV8l1tZ50gecT13"))
        reference_order_id = client.order.create(data)
        print(reference_order_id)
        order_id_dict = {
            "amount": str(amount),
            "order_id": str(reference_order_id['id'])
            
            
        }
        
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount, currency=currency, reference_order_id=reference_order_id['id'])

        order.save()

        print('order ------', order)
        print(email)
        print(order.email)
        # Payment params:
        payment_params = {
            "amount" : int(str(amount)+'00'),
            "order_id": str(reference_order_id['id']),
            "name": order.name,
            "email": order.email, 
            "address":order.address
        } 
        print(payment_params['order_id'])


        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")


        # Razorpay Order create
        # client = razorpay.Client(auth=("rzp_test_dgzzcZxUBrkJSW", "XOWQ750mgHV8l1tZ50gecT13"))
        print('client -------------', client)
        print(str(amount))

        # client.order.create(amount=order.amount, currency=currency, payment_capture = 1, order_id = order.order_id)
        # # print('response_id--------------------',response_id)
        
        # order_id_dict = {
        #     "amount": str(Orders.amount),
        #     "order_id": str(response_id)
        # }
        # client.order.create(data=order_id_dict, currency=currency, payment_capture = 1, order_id = order.order_id)
        # print('response_id--------------------',response_id)
        

        update.save()
        # PAY WITH RAZORPAY FORM
        keyid = 'rzp_test_dgzzcZxUBrkJSW'
        buttontext = 'Pay With Razorpay'
        CompanyName = 'Ecommerce Website'
        description = 'Ecommerce Website Created By Arpit Gupta'
        image = 'shop/images/default_0Qe05Gg.jpeg'
        prefillname = 'Arpit Gupta'
        prefillemail = 'arpit.gupta@unthinkable.co'
        name = request.POST.get('id', '')
        pay =  PayWithRazorpay(keyid=keyid, amountPWR=amount, currencyPWR='INR', reference_order_idPWR=reference_order_id['id'], buttontext=buttontext, CompanyName=CompanyName, description=description, image=image, prefillname=prefillname, prefillemail=prefillemail, name = name)
        pay.save()
        # print(pay)
        print(reference_order_id['id'])



        thank = True
        id = order.order_id
        # refer_order_id  = order.reference_order_id
        # print(refer_order_id)
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        return render(request, 'shop/razorpay.html',{'payment_params': payment_params})
    
    return render(request, 'shop/checkout.html')


def handleSignup(request):
    if request.method == 'POST':
        #Get all Post field
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        mobilenumber = request.POST['mobilenumber']
        profilepicture = request.POST['profilepicture']
        pass1 = request.POST['pass1']
        pass2= request.POST['pass2']

        # Check for error in all fields
        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters")
            return redirect('shophome')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('shophome')


        if pass1!=pass2:
            messages.error(request, "Password do not match")
            return redirect("shophome")



        # Create User
        myuser = User.objects.create(username=username, first_name= first_name, last_name = last_name, email=email,mobilenumber=mobilenumber,profilepicture=profilepicture, password=make_password(pass1))
        # myuser.first_name = fname
        # myuser.last_name = lname 
        # myuser.mobilenumber = request.POST('mobilenumber')
        # myuser.profilepicture = request.POST('profilepicture')
        
        myuser.save()
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        messages.success(request, "Your account has been successfully created")
        return redirect('shophome')
        

        

    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        #Get all Post field
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            messages.success(request, "Successfully Logged In")
            return redirect('shophome')

        else:
            # alert("Invalid Credential, Please try again")
            print('??????????????????????????')
            messages.error(request, 'Invalid Credential, Please try again')
            template='shophome'
            return redirect(template)
    return HttpResponse('404 - NOT FOUND')

def handleLogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('shophome')
    
def checkout_summary(request):
    order = Orders.objects.latest('order_id')
    # print(order.objects.all())
    # print(order)
    params = {
        'order' : order
    }
    return render(request, 'shop/checkout_summary.html', params)

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.created_at})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def handlerazorpay(request):
    if request.method=='post':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        secret = 'XOWQ750mgHV8l1tZ50gecT13'
        print('8888888888888888888888888888',razorpay_payment_id, razorpay_order_id, razorpay_signature )

        generated_signature = hmac_sha256(razorpay_order_id + "|" + razorpay_payment_id, secret);  
        if (generated_signature == razorpay_signature):
            return HttpResponse('PAYMENT is SUCCESSFUL')

    return HttpResponse('DONE!')