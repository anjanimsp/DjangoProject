from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order
from math import ceil

# Create your views here.

def index(request):
    #products=Product.objects.all()
    #print(products)
    #n=len(products)
    #nSlides=n//4+ceil((n/4)-(n//4))
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    #params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    #allprods=[[products,range(1,nSlides),nSlides],
    #          [products,range(1,nSlides),nSlides] 
    #         ]
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)



def contact(request):
    if request.method =='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        #print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')


def about(request):
    return render(request,'shop/about.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
   return render(request,'shop/search.html')

def prodView(request,myid):
    #Fetch the product using ID
    product=Product.objects.filter(id=myid)
    #print(product)

    return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    if request.method =='POST':
        item_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address1=request.POST.get('address1','')
        address2=request.POST.get('address2','')
        address=address1+" "+address2
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')

        #print(name,email)
        order=Order(item_json=item_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
            
    return render(request,'shop/checkout.html')

