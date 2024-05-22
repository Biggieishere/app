from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from login.models import review,blog,chat
from django.utils.html import escape
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request,"homepage.html")

def loginapp(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        
        if user is not None:
            messages.success(request, "Logged in successfully.")
            login(request,user)
            return redirect("/blog")
            
            
        else:
            messages.error(request, "Login failed. Incorrect username or password")
    
    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        sanitized_input = escape(username)
        
        if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
        
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
           
        else:
            users = User.objects.create_user(username=sanitized_input,email=email,password=password)
            users.save()

            messages.success(request, "Signed in successfully")
            return redirect("/login")
        
        
            
    return render(request,"signup.html")
   
   
@login_required     
def review_ins(request):
    if request.method == "POST":
        review_instance = request.POST.get('review')
        
        sanitized_review = escape(review_instance)

        user = request.user
        ins = review(review=sanitized_review, user=user)
        ins.save()
        messages.success(request, 'Review submitted')
        
    
    
    
    return render(request,"review.html")


def veiwsection(request):
    reviews = review.objects.all()
    return render(request, 'viewing.html', {'reviews': reviews})
    
 
    

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect("/")


@login_required
def Blog(request):
    blog_view = blog.objects.all()
    context = {'blogging':blog_view}
    return render(request,"blog.html",context)


def Blogspot(request,slug):
    blogs = blog.objects.filter(slug=slug).first()
    context = {'blog':blogs}
    return render(request,"blogspot.html",context)

@login_required
def chat_room_sel(request):
    return render(request,"chat_rooms.html")


@login_required
def chat_room_chat(request):
    
    if request.method == "POST":
        messages = request.POST.get('messages')
        sanitized_input = escape(messages)
        user = request.user
        msg = chat(messages=sanitized_input,user=user)
        msg.save()
        return redirect("/rooms")
        
    
    
    chat_messages = chat.objects.all()
    contextual = {'mess':chat_messages}


    return render(request,"chatting.html",contextual)


