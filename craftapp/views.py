from django.shortcuts import render, redirect
from .models import Coordinate
from django.shortcuts import get_object_or_404
from .forms import CoordinateForm, WorldForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
#ここからQiita記事抜粋
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from . forms import UserCreateForm, LoginForm



def index(request):
    coordinates = Coordinate.objects.all().order_by('created_date')
    #{'coordinates': coordinates}の部分がhtmlの{% for coordinate in coordinates %}に対応している。
    return render(request, 'craftapp/index.html', {'coordinates': coordinates})

#座標情報の詳細を表示する。
@login_required
def coordinate_detail(request, coordinate_id):
  coordinate = get_object_or_404(Coordinate, id=coordinate_id)
  return render(request, 'craftapp/coordinate_detail.html', {'coordinate': coordinate})

#新しい座標を登録する。
@login_required
def new_coordinate(request):
    form = CoordinateForm
    #入力フォームに座標を入力して、送信ボタンを押したときの処理
    if request.method == "POST":
      form = CoordinateForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('craftapp:index')
    
    #ただ単に入力フォームを開くときの処理
    else:
      form = CoordinateForm
    return render(request, 'craftapp/new_coordinate.html', {'form': form })

#POSTの時だけ、関数を実行する。
@require_POST
@login_required
def delete_coordinate(request, coordinate_id):
  coordinate = get_object_or_404(Coordinate, id=coordinate_id)
  coordinate.delete()
  return redirect('craftapp:index')

def edit_coordinate(request, coordinate_id):
  coordinate = get_object_or_404(Coordinate, id=coordinate_id)
  if request.method == "POST":
    form = CoordinateForm(request.POST, instance=coordinate)
    if form.is_valid():
      form.save()
      return redirect('craftapp:index')

  else:
    form = CoordinateForm(instance=coordinate)
    #編集するために登録しているインスタンスを呼び出す。
    return render(request, 'craftapp/edit_coordinate.html', {'form':form, 'coordinate':coordinate})


#新しいプレーヤーを登録する。
@login_required
def new_player(request):
    form = PlayerForm
    #入力フォームに座標を入力して、送信ボタンを押したときの処理
    if request.method == "POST":
      form = PlayerForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('craftapp:index')
    
    #ただ単に入力フォームを開くときの処理
    else:
      form = PlayerForm
    return render(request, 'craftapp/new_player.html', {'form': form })

#新しいワールドを登録する。
@login_required
def new_world(request):
    form = WorldForm
    #入力フォームに座標を入力して、送信ボタンを押したときの処理
    if request.method == "POST":
      form = WorldForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('craftapp:index')
    
    #ただ単に入力フォームを開くときの処理
    else:
      form = WorldForm
    return render(request, 'craftapp/new_world.html', {'form': form })

#ここからQiita記事抜粋
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る。
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る。
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'craftapp/create_account.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'craftapp/create_account.html', {'form': form})

create_account = Create_account.as_view()

class Account_login(View):
  def post(self, request, *args, **kwargs):
    form = LoginForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      user = User.objects.get(username=username)
      login(request, user)
      return redirect('/')
    return(request, 'craftapp/account_login.html', {'form':form})

  def get(self, request, *args, **kwargs):
    form = LoginForm(request.POST)
    return render(request, 'craftapp/account_login.html', {'form': form})

account_login = Account_login.as_view()

