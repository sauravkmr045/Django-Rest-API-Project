from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsReadOnly(BasePermission):

	def has_permission(self,request,view):
		if request.method  in SAFE_METHODS:
			return True
		else:
			return False


class IsGETOrPatch(BasePermission):

	def has_permission(self,request,view):
		allowed_methods = ['GET','PATCH']
		if request.method  in allowed_methods:
			return True
		else:
			return False

class AllforAdmin(BasePermission):

	def has_permission(self,request,view):
		user = request.user.username
		allowed_methods = ['GET','PATCH','POST','PUT','DELETE']
		if user.lower() == 'admin':
			if request.method  in allowed_methods:
				return True
		elif user != ' ' and len(user)%2==0:
			if request.method in SAFE_METHODS:
				return True

		else:
			return False