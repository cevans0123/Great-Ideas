from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib import messages
from django.contrib.auth import logout
from time import gmtime, strftime
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'great_ideas/index.html')

def login(request):#LOGIN   
    result = User.objects.log_validator(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['log_email'])
        request.session['user_id'] = user.id      
    return redirect('/ideas')

def create(request):#REG new user
    result = User.objects.reg_validator(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/') 
    else:
        hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashedpw)
        user = User.objects.last()
        request.session['user_id'] = user.id
    return redirect('/ideas')

def ideas(request):
    context = {
        'ideas' : Idea.objects.all(),
        'user' : User.objects.get(id = request.session['user_id']),   
        'likes' : Idea.objects.filter   
    }
    return render(request, 'great_ideas/ideas.html', context)

def like(request, idea_id):




    
    user = User.objects.get(id = request.session['user_id'])
    idea = Idea.objects.filter(id = idea_id)
    idea.likes.add(the_user)
    idea.save()
    return redirect ('/ideas')

# def unlike(request, idea_id):
#     the_user = User.objects.get(id = request.session['user_id'])
#     the_idea = Idea.objects.filter(id = idea_id)
#     the_idea.likes.delete(the_user)
#     the_idea.save()
#     return redirect ('/ideas')    

def new(request):

    return render(request, 'great_ideas/new.html')
    
def add(request):
    if len(request.POST['content']) < 10:   
        messages.error(request, "Idea must be at least 10 characters.")
        return redirect('/new') 
    else: 
        if request.method == "POST":
            idea = Idea.objects.create(content = request.POST['content'], posted_id= request.session['user_id'])
            return redirect("/ideas")
        else:
            return redirect("/ideas")  

def view(request, id):
    idea = Idea.objects.get(id = id)
    context = {
        'idea' : idea,
    }
    return render(request, 'great_ideas/view.html', context)  

def edit(request, id):
    idea = Idea.objects.get(id = id)
    context = {
        'idea' : idea,
    }
    return render(request, 'great_ideas/edit.html', context)  

def update(request, id):
    x = str(id)
    result = User.objects.validator(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect(x+'/edit') 
    else:
        b = Idea.objects.get(id=id)
        b.content = request.POST['content']
        b.save()
    return redirect('/ideas')

def delete(request, idea_id):
    Idea.objects.get(id= idea_id).delete()
    return redirect('/ideas')

def logout_user(request):
    request.session.flush()
    return redirect('/')    