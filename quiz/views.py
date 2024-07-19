from django.shortcuts import render, redirect
from .models import schedule

# Create your views here.
def index(request):
    data = schedule.objects.all()
    results = {"data":data}
    return render(request, "index.html", results)

def addTask(request):
    return render(request, "addTask.html")

def insert_data(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['desc']
        priority = request.POST['priority']
        date = request.POST['ddate']
        status = "Not completed"
        print(name, description, priority, date, status)

        query = schedule(Task=name, Description=description, Priority=priority, DueDate=date, Status=status)
        query.save()

        return redirect("/")
   
    return render(request, "addTask.html")

def update_data(request, id):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['desc']
        priority = request.POST['priority']
        date = request.POST['ddate']
        status = request.POST['status']

        edit=schedule.objects.get(id=id)
        edit.Task=name
        edit.Description=description
        edit.Priority=priority
        edit.DueDate=date
        edit.Status=status
        edit.save()
        return redirect("/")
    
    data=schedule.objects.get(id=id)
    results = {"data":data}
    return render(request, "update.html", results)

def delete_data(request, id):
    data=schedule.objects.get(id=id)
    data.delete()
    return redirect("/")