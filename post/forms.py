from django import forms
from .models import Post ,Event


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','image']

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['event_name','event_detail','event_pic','startdate_event','enddate_event']