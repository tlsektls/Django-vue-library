from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from .models import CustomUser


from rest_framework import generics
from rest_framework.response import Response

class UserIndex(generics.RetrieveAPIView):
  queryset = CustomUser.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()

    serializer = BookInstanceSerializer(queryset, many=True)
    return Response(serializer.data)


 
def index(request):
    context = {}
    # context['m_id'] = request.session['m_id']
    # context['m_name'] = request.session['m_name']
 
    # m_id 세션변수 값이 없다면 '' 을 넣어라
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')
 
    return render(request, 'user/index.html', context)
 
 
def user_reg(request):
    if request.method == "GET":
        return render(request, 'user/user_reg.html')
    elif request.method == "POST":
        context = {}
        user_id = request.POST["user_id"]
        passwd = request.POST["passwd"]
        name = request.POST["name"]
        email = request.POST["email"]
 
        # 회원가입 중복체크
        rs = CustomUser.objects.filter(user_id=user_id)
        if rs.exists():
            context['message'] = user_id + "가 중복됩니다."
            return render(request, 'user/user_reg.html', context)
 
        else:
            CustomUser.objects.create(
                user_id=user_id, passwd=passwd,  name=name, email=email, usage_flag='y',
                reg_date=datetime.now(), update_date=datetime.now())
            context['message'] = name + "님 회원가입 되었습니다."
            return render(request, 'user/index.html', context)
 
 
def user_login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    elif request.method == "POST":
        context = {}
 
        user_id = request.POST.get('user_id')
        passwd = request.POST.get('passwd')
 
        # 로그인 체크하기
        rs = CustomUser.objects.filter(user_id=user_id, passwd=passwd).first()
        print(user_id + '/' + passwd)
        print(rs)
 
        #if rs.exists():
        if rs is not None:
 
            # OK - 로그인
            request.session['m_id'] = user_id
            request.session['m_name'] = rs.name
 
            context['m_id'] = user_id
            context['m_name'] = rs.name
            context['message'] = rs.name + "님이 로그인하셨습니다."
            return render(request, 'user/index.html', context)
 
        else:
 
            context['message'] = "로그인 정보가 맞지않습니다.\\n\\n확인하신 후 다시 시도해 주십시오."
            return render(request, 'user/login.html', context)
 
 
def user_logout(request):
    request.session.flush()
    return redirect('/user/')
