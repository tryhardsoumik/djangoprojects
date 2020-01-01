from django.shortcuts import render,redirect
from polls.models import Tasklist
from polls.form import TaskForm
from django.contrib import messages
# Create your views here
def index(request):
    if request.method=="POST":# when I add some task on the field it will see the forms.py
        form=TaskForm(request.POST or None)#pass the post request in TaskForm connect to TaskForm
        if form.is_valid():# check the validity
            form.save()
        messages.success(request,("New Task Added"))    # for popup messages after adding tasks
        return redirect('index')   
    else:


            all_tasks=Tasklist.objects.all #this will help to fetch all the objects from model and now this is instance
            return render(request,'index.html',{'all_tasks':all_tasks}) # this contains dictionary and i have to create to pass

#delete function to delete tasks here you have to pass the task_id u want to delete and then you pass 
# the primary key task_id and assign it into your variable and return to index page by render

def delete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('index')
# now create edit_task function

def edit_task(request,task_id):
    if request.method=="POST": #when you click on edit lecture it will trigger a post request
        task=Tasklist.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)#updating as i have a taskid database will recognize

        
        if form.is_valid():
            form.save()
        messages.success(request,("Task edited"))    
        return redirect('index')   
    else:


            task_obj=Tasklist.objects.get(pk=task_id)
            return render(request,'edit.html',{'task_obj':task_obj}) 


def complete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.done=True
    task.save()

    return redirect('index')

def pending_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.done=False
    task.save()

    return redirect('index')



def contact(request):
    context={
"contact_text":"this is contact page",


    }
    return render(request,'contact.html',context)
        
def Aboutus(request):
    context={

"Aboutus_text":"this is AboutUs page",

    }
    return render(request,'Aboutus.html',context)
    
    