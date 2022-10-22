from django.shortcuts import render,redirect
from .models import ImageUpload
from .forms import ImageForm
# Create your views here.
def index(request):
    images =ImageUpload.objects.all()
    form = ImageForm()
    if request.method == 'POST':
        form =ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        'images' : images,
        'form' : form,
    }
    return render(request,'myapp/index.html',context)

def delete(request,pk):
    image=ImageUpload.objects.get(id=pk)
    if request.method=='POST':
        image.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')