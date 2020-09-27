from .models import Chat

def chat(request):
    if request.method == 'POST':
        if request.user.is_staff:
            user = request.user
            auth = Authority.objects.get(authUser = user)
            content = request.POST.get('content')
            Chat.objects.create(writer = user, auth = auth, content = content)
            chat = Chat.objects.filter(auth = auth)[::-1]
            return render(request, 'loginsignup/chatauth.html',{'chat':chat, 'usr':user.username})
        if request.user.is_active:
            user = request.user
            emp = Employee.objects.get(empUser = user)
            auth = emp.senior       
            content = request.POST.get('content')
            Chat.objects.create(writer = user, auth = auth, content = content)    
            chat = Chat.objects.filter(auth = auth)[::-1]
            return render(request, 'loginsignup/chatemp.html',{'chat':chat, 'usr':user.username})
    if request.user.is_staff:
        user = request.user
        auth = Authority.objects.get(authUser = user)
        chat = Chat.objects.filter(auth = auth)[::-1]
        return render(request, 'loginsignup/chatauth.html',{'chat':chat, 'usr':user.username})
    elif request.user.is_active :
        user = request.user
        emp = Employee.objects.get(empUser = user)
        auth = emp.senior
        chat = Chat.objects.filter(auth = auth)[::-1]
        return render(request, 'loginsignup/chatemp.html',{'chat':chat, 'usr':user.username})
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))