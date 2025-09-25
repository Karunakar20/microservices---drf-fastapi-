from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny

from user.services.user_login_logout import UserLoginorLogout

class UserViewLogin(APIView):
     permission_classes = [AllowAny]
     
     def post(self, request):
          
          data = request.data
          
          pdata = {
               'data':data,
          }
          
          response = UserLoginorLogout(pdata).login()
          
          return Response(response.toJson())
     
class UserViewLogout(APIView):
     
     def post(self, request):
          
          data = request.data
          
          pdata = {
               'data':data,
          }
          
          response = UserLoginorLogout(pdata).logout()
          
          return Response(response.toJson())