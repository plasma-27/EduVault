from argon2 import PasswordHasher, exceptions


class passFunc:
   
   def __init__(self,key,secret,password): 
      self.password=password
      self.ph = PasswordHasher()
      

   def generateBoilpass(self):
   #  porridge = Porridge(self.keySecret)  #Generate porridge instance 
   #  boiled_password = porridge.boil(self.password)
      boiled_password = self.ph.hash(self.password)
      return boiled_password
    

   def passVerify(self,rawPassword,boiledPassword):
   #   porridge = Porridge(self.keySecret)
   #   verified = porridge.verify(rawPassword,boiledPassword)
     try: 
      verified = self.ph.verify(boiledPassword, rawPassword) 
      return verified
     except exceptions.VerifyMismatchError:
            return False 
  
     

        
