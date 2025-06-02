from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Note

# Create your views here.
# def renderSomething(req):
#     return render(req,"index.html")
# def aboutSomething(req):
#     return HttpResponse("My About Section")

def indexView(req):
    notes = Note.objects.all()
    return render(req,"index.html", context={
        'notes':notes
    })

def aboutView(req):
    return render(req,"about.html")

def saveDataView(req):
    print(req.POST)
    # title = req.POST.get("title")
    title = req.POST.get("title","")
    name = req.POST.get("name","")
    description = req.POST.get("description","")

    if not title or not description or not name:
        # error show karna hai
        messages.error(req,"Fill All Details")
        return redirect("/")
    
    note = Note(title=title, name=name, description=description)
    note.save()
    #Data saved
    messages.success(req,"Detail saved")
    return redirect("/")
    # return HttpResponse(f"Title= {req.POST.get("title")} description = {req.POST.get("description")}")
    # return HttpResponse(f"Details saved")

# delete vieww with unique primary key

def deleteView(req,id):

    note = Note.objects.get(id=id)
    note.delete()
    messages.success(req,"Note Deleted")

    return redirect("/")


def updateViewPage(req,id):
    note = Note.objects.get(id=id)
    if req.method == 'POST':
        title = req.POST.get("title","")
        name = req.POST.get("name","")
        description = req.POST.get("description","")
        published = req.POST.get("published","")
        published = True if published == 'on' else False
        print(published)
        if not title or not name or not description:
            messages.error(req,"Fill All Details")
        else:
            note.title = title
            note.name = name
            note.description = description
            note.isPublish = published
            note.save()
        messages.success(req,"Details Updated !")

    return render(req,"edit_page.html",context={"note":note})