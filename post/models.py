from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, default=1)
	title = models.CharField(max_length=255)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)
	image =  models.ImageField(upload_to="blog_images", null=True , blank=True)
	slug = models.SlugField(unique=True, null=True)
	publish = models.DateField()
	draft = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def get_absoulute_url(self):
		return reverse("post:detail", kwargs={"slug": self.slug})
	def search_id(self, x ):
		s = Post.objects.all().filter(title=x)
		return reverse("post:detail", kwargs={"slug": self.slug})
	def update_url_post(self):
		return reverse("post:update", kwargs={"slug": self.slug})
	def delete_url(self):
		return reverse("post:delete", kwargs={"slug": self.slug})
	def create_url(self):
		return redirect("post:create")
	def croping(self):
		return str(self.content[0:30])
		pass
	def name_val(self):
		return str(self.slug) 
		pass
	class Meta:
		ordering = ['-timestamp','-updated']

class Event(models.Model):
	event_author = models.ForeignKey(User, default=1)
	event_slug = models.SlugField(unique=True, null=True)
	event_name = models.CharField(max_length=160)
	event_detail = models.TextField()
	event_pic = models.ImageField(upload_to="blog_images", null=True , blank=True)
	startdate_event = models.DateField(null=True)
	enddate_event = models.DateField(null=True)
	def __str__(self):
		return self.event_name
	class Meta:
		ordering = ['startdate_event','enddate_event']

def post_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		slug=slugify(instance.title)
		qs= Post.objects.filter(slug=slug).order_by("-id")
		if qs.exists():
			slug= "%s-%s"%(slug , instance.id)
		instance.slug = slug 
		instance.save()
def event_reciever(sender, instance , *args, **kwargs):
	if not instance.event_slug:
		slug= slugify(instance.event_name)
		qs= Event.objects.filter(event_slug=slug).order_by("-id")
		if qs.exists():
			slug = "%s-%s"%(slug, instance.id)
		instance.event_slug= slug
		instance.save()
post_save.connect(event_reciever,sender=Event)
post_save.connect(post_reciever,sender=Post)