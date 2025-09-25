from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from user.utilities.common import Response,ResponseType

class UserLoginorLogout:
     
     def __init__(self,uData):
          
          self.data = uData['data']
          
     def __reqData(self):
          self.user_name = self.data.get('username')
          self.password = self.data.get('password')
          self.refresh_token = self.data.get('refresh')
          self.access_token = self.data.get('access_token')
          
     def login(self):
          self.__reqData()
          
          user = authenticate(username=self.user_name, password=self.password)
          
          if user:
               refresh = RefreshToken.for_user(user)
               
               context = {
                    "username": user.username,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
               }
               
               return Response(True,ResponseType.success,None,None,context)
          
          else:
               return Response(True,ResponseType.success,None,None,"Details are not found, Please do register")
          
     def logout(self):
          self.__reqData()
          
          token = RefreshToken(self.refresh_token)
          token.blacklist()
          
          if self.access_token:
               access = AccessToken(self.access_token)
               access.blacklist()
          
          return Response(True,ResponseType.success,None,None,"Logout")
          