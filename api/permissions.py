from rest_framework.permissions import BasePermission
from django.utils import timezone


class AuthorOrStaff(BasePermission):
	message = "you must be the author of this post"


	def has_object_permission(self, request , view, obj):
		date = timezone.now().date()
		
		if obj.draft or obj.publish > date:
			if request.user.is_staff or request.user.is_superuser or (obj.author == request.user):
				return True
			else:
				return False
		else:
			return True

