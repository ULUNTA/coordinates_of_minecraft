from django.forms import ModelForm
from .models import Coordinate, World
#↓Qiita記事より抜粋
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CoordinateForm(ModelForm):
    class Meta:
        #model.pyのclassを継承している。
        model = Coordinate
        #入力フォームのフィールドを定義する。これもモデルから継承している。
        fields = ['world', 'player', 'place', 'x_coordinate', 'y_coordinate', 'z_coordinate' ]

class WorldForm(ModelForm):
    class Meta:
        model = World
        fields = ['world']

#↓Qiita記事より抜粋
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にする。
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2",)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示変更を可能に。
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

