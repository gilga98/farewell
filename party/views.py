from django.shortcuts import render
from .models import Feedback,Gotcha,Oqp,Sorry,WishingWell
# Create your views here.


def index(request):
    if request.method=="GET":
        return render(request,'index.html',{'all_feedbacks':Feedback.objects.all()})

    if request.method=="POST":
        name=request.POST.get('feedback_name',None)
        feedback=request.POST.get('feedback',None)
        feedback_instance=Feedback.objects.create(name=name,feedback=feedback)

        context={'your_feedback':feedback_instance,
                 'all_feedbacks':Feedback.objects.all()}
        return render(request,'index.html',context)


def gotcha(request):
    if request.method=="GET":
        return render(request,'gotcha.html',{'all_gotchas':Gotcha.objects.all()})

    if request.method=="POST":
        secret=request.POST.get('secret',None)
        gotcha_instance=Gotcha.objects.create(secret=secret)
        gotcha_instance.save()
        context={'your_gotcha':gotcha_instance,
                 'all_gotchas':Gotcha.objects.all(),}
        return render(request,'gotcha.html',context)



def oqp(request):
    if request.method=="GET":
        return render(request, 'oqp.html', {'oqps': Oqp.objects.all()})

    if request.method=="POST":
        recipient=request.POST.get('questo',None)
        question=request.POST.get('onequestion',None)
        oqp_instance=Oqp.objects.create(recipient=recipient,question=question)

        context={
            'your_question':oqp_instance,
            'oqps':Oqp.objects.all()
        }

        return render(request,'oqp.html',context)



def wishingwell(request):
    if request.method=="GET":
        return render(request, 'wishwell.html', {'wishes': WishingWell.objects.all()})

    if request.method=="POST":
        name=request.POST.get('wisher_name',None)
        crush_desc=request.POST.get('crush_desc',None)
        ww_instance=WishingWell.objects.create(name=name,crush_desc=crush_desc)

        context={
            'your_wish':ww_instance,
            'wishes':WishingWell.objects.all()
        }
        return render(request,'wishwell.html',context)



def sorry(request):
    if request.method=="GET":
        return render(request, 'sorry.html', {'sorries': Sorry.objects.all()})

    if request.method=="POST":
        name=request.POST.get('sorry_from',None)
        sorry_desc=request.POST.get('sorry_desc',None)
        to=request.POST.get('sorry_to',None)

        sorry_instance=Sorry.objects.create(name=name,sorry=sorry_desc,to=to)

        context={
            'your_sorry':sorry_instance,
            'sorries':Sorry.objects.all(),
        }
        return render(request,'sorry.html',context)
