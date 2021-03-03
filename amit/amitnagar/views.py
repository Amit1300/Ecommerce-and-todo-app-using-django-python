from django.shortcuts import render,HttpResponse,redirect
from amitnagar.serializer import Serializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.conf import settings 
from django.core.mail import send_mail 
from django.utils.decorators import method_decorator


from .models import *
from .forms import Todoform

def home_view(request): 
    task=Todolist.objects.all()
    context ={"task":task} 
    context["form"]=Todoform()


    if(request.method=="POST"):
        form=Todoform(request.POST)
       
        if form.is_valid():
            form.save()

        else:
            return redirect("/")
    

    return render(request,"home.html", context) 

def show(request,pk):
    task=Todolist.objects.get(id=pk)
    form=Todoform(instance=task)
    if request.method=="POST":
        form=Todoform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            
        return redirect("/")
    context={"form":form}
    return render(request,"show.html" ,context)    


def deleteTask(request,pk):
    item=Todolist.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("/")
    context={"item":item}
    return render(request,"delete.html",context)

@api_view(["GET"])
def apiview(request):
    task=Todolist.objects.all()
    Serializers=Serializer(task,many=True)
    return Response(Serializers.data)


@api_view(["GET"])
def taskDetails(request,pk):
    task=Todolist.objects.get(id=pk)
    Serializers=Serializer(task,many=False)
    return Response(Serializers.data)


def index(request):

    categories=Category.objects.all()
    category_id=request.GET.get("category")
    print(request.session.get("email"))
    if category_id:
        products=Product.objects.filter(category=category_id)
    else:
        products=Product.objects.all()
    context={"products":products,"categorys":categories}
    cart=request.session.get("cart")
    if not cart:
        request.session["cart"]={}
    else:
        pass
    return render(request,"base.html",context)

def signup(request):
    print(request.POST)
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone_no=request.POST.get("phone")
        password=request.POST.get("password")
        customer=Customer(name=name,email=email,phone_no=phone_no,password=password)
        customer.save()
        context={"form":customer}
        return redirect("/")
    return render(request,"signup.html")

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        email=request.POST.get("email")
        password=request.POST.get("password")
        customer=Customer.objects.get(email=email)
        error_message=None
        message="welcome to website"
        if customer.password==password:
            request.session["email"]=customer.email
            request.session["customer"]=customer.id
            return redirect("/")
        else:
            error_message="invalid password or email!! "

        return render (request,"login.html",{"error":error_message,"message":message})



def cartvalue(request):
    product=request.POST.get("products")
    cart=request.session.get("cart")
    remove=request.POST.get("remove")
    add=request.POST.get("add")
    print(product)
    if cart:
        quantity=cart.get(product)
        if quantity:
            if remove:
                if quantity<=1:
                    cart.pop(product)
                else:
                    cart[product]=quantity-1
            else:
                cart[product]=quantity+1
        else:
            cart[product]=1
    else:
        cart={}
        cart[product]=1
    request.session["cart"]=cart
    return redirect("/")
    
def logout(request):
    request.session.clear()
    return redirect("/login")





def cart(request):
    ids=list(request.session.get("cart").keys())
    products=Product.objects.filter(id__in=ids)
    context={"products":products}
    return render(request,"cart.html",context)



def checkout(request):
    address=request.POST.get("address")
    phone=request.POST.get("phone")
    customer=request.session.get("customer")
    cart=request.session.get("cart")
    id=list(cart.keys())
    products=Product.objects.filter(id__in=id)
    
    print(customer,address,phone,cart,products)
    for product in products:
        order=Order(
            customer=Customer(id=customer),
            phone=phone,
            address=address,
            product=product,
            quantity=cart.get(str(product.id)),
            price=product.price
        )
        order.placeorder()
    request.session["cart"]={}

    return redirect("/")






# def auth_middleware(get_response):
#         # One-time configuration and initialization.

#     def middleware(request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         print("amit kumar nagar")
#         if not request.session.get('customer'):
#             return ("/login")

#         response = get_response(request)

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response

#     return middleware

