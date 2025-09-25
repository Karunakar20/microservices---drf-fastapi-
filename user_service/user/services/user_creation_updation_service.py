from user.utilities.common import Response,ResponseType
from django.db import transaction

from user.models import User
from user.serializer.users_serializer import UserSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()

class UserCreateOrUpdateService:
     def __init__(self,uData):
          self.data = uData['data']
          self.cmd = uData['cmd']
          
     def __reqData(self):
          self.id = self.data.get('id')
          self.username = self.data.get("username",None)
          self.first_name = self.data.get("first_name",None)
          self.last_name = self.data.get("last_name",None)
          self.password = self.data.get("password",None)
          self.phone_number = self.data.get("phone_number",None)
          
     def __createOrUpdate(self):
          
          try:
               with transaction.atomic():
                    
                    if self.id:
                        user = User.objects.get(id=self.id)
                    else:
                         user = User()
                         
                    user.username = self.username
                    user.first_name = self.first_name
                    user.last_name = self.last_name
                    user.phone_number = "+91"+" "+self.phone_number
                    user.set_password(self.password)
                    user.save()

                    return Response(True,ResponseType.success,self.msg)
                                             
          except Exception as e:
               return Response(False,ResponseType.err,None,str(e))
          
          
     def __getUsers(self):
          
          if self.id:
               user_res = UserSerializer(User.objects.get(id=id)).data
               
               context = {
                    'data':user_res
               }
               
               return Response(True,ResponseType.success,None,None,context)
          
          else:
               users = User.objects.all()
               
               user_res = UserSerializer(users,many=True).data
               
               context = {
                    'data':user_res
               }
               
               return Response(True,ResponseType.success,None,None,context)
          
                         
     def manage(self):
          self.__reqData()
          
          match self.cmd:
               case 'create':
                    self.msg = f"{self.username} created successfully"
                    return self.__createOrUpdate()
                    
               case 'update':
                    self.msg = f"{self.username} updated successfully"
                    return self.__createOrUpdate()
               
               case _:
                    return Response(False,ResponseType.err,"Invalid cmd")
               
     def get(self,id):
          self.id = id
          
          match self.cmd:
               
               case 'get_all':
                    return self.__getUsers()
                    
               case 'get_by_id':
                    return self.__getUsers()
               
               case _:
                    return Response(False,ResponseType.err,"Invalid cmd")
                    
                    
          
          
          
          
          
          
          
               
          