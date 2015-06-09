from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http.request import QueryDict
from app_user.models import AppUser
from django.db.models import Q


class SignUpAPI(APIView):

    allowed_signup_methods = {
        'email': '_signup_using_email',
        'facebook': '_signup_using_facebook',
        'twitter': '_signup_using_twitter'
    }
    def post(self, request, *args, **kwargs):
        post_data = request.POST

        try:
            signup_method = post_data.get('signup_method')
            if signup_method in self.allowed_signup_methods:
                return getattr(self, self.allowed_signup_methods[signup_method])(post_data)
            else:
                return Response({'status': 204, 'error': {'message': 'Invalid signup method'}})    
        except Exception as e:
            return Response({'status': 204, 'error': {'message': str(e)}})

    def _signup_using_email(self, post_data):
        (validation_status, message) = self._validate_post_data(post_data)
        if validation_status:
            return Response({'status': 200, 'success': message})
        else:
            return Response({'status': 204, 'error': {'message': message}})
    

    def _validate_post_data(self, post_data):
        from django.core.validators import validate_email
        email = post_data.get('email', None)
        phone = post_data.get('phone', None)
        username = post_data.get('username', None)
        password = post_data.get('password', None)

        if not (email and phone and username and password):
            return False, 'Please fill all the fields.'
        try:
            validate_email(email)
        except:
            return False, 'Invalid Email'
        users = AppUser.objects.filter(Q(user__username=username) | Q(user__email=email) | Q(phone=phone))
        if users.count():
            return False, 'Users with given username/email/phone exist'
        else:
            return True, 'Validated'
        

    def print_data(self, data_obj):
        
        if type(data_obj) in (unicode, str, int):
            return HttpResponse(data_obj)
        if type(data_obj) in (QueryDict, dict) :
            return Response(data_obj)
        else:
            import json
            from django.core import serializers as sl
            data = sl.serialize('json', [data_obj,])
            struct = json.loads(data)
            data = json.dumps(struct[0])
            return HttpResponse(data, mimetype='application/json')


#     def 
#         serializer = RegistrationDataSerializer(request.POST)
#         if serializer.is_valid():
#             return JSONResponse(data=serializer.data)
#         else:
#             return Response({'error' : 'eerer'})
#         return HttpResponse('Unauthorized', status=200)        
#         users = AppUser.objects.all()
#         
#         serializer = AppUserSerializer(users, many=True)
#         return JSONResponse(request.user)

#     def get(self, request, *args, **kwargs):      
#         serializer = UserSerializer(request.user)
#         data = serializer.data
#        return JSONResponse(request.user.is_authenticated())
    


class AuthView(APIView):
    """
    Authentication is needed for this methods
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 
    def get(self, request, format=None):
        return Response({'detail': request.user})

