from django import forms
from .models import Post ,Event
from django.contrib.auth.models import User 


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','image','publish','draft']
		widgets={
		        'publish': forms.DateInput(attrs={"type":"date"}),
		        }
class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['event_name','event_detail','event_pic','startdate_event','enddate_event']
		widgets={
		        'startdate_event': forms.DateInput(attrs={"type":"date"}),
		        'enddate_event': forms.DateInput(attrs={"type":"date"}),
		        }
class UserSignUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		widgets= {
			'password': forms.PasswordInput(),
		}
class UserLogin(forms.Form):
	username= forms.CharField(required=True)
	password= forms.CharField(required=True,widget=forms.PasswordInput())
