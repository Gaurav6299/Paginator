from django.shortcuts import render
from.models import Detail
from django.core.paginator import Paginator
# Create your views here.
def StudentData(request):
    stu=Detail.objects.all()
    p=Paginator(stu,4)
    page_number=request.GET.get('page')
    print(page_number)
    page_obj=p.get_page(page_number)
    return render(request,'index.html',{'stu':page_obj})



