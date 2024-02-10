from porridge import Porridge

class passFunc:
   
   def __init__(self,key,secret,password):
      self.key=key
      self.secret=secret 
      self.password=password
      self.keySecret = key+':'+secret

   def generateBoilpass(self):
    porridge = Porridge(self.keySecret)  #Generate porridge instance 
    boiled_password = porridge.boil(self.password)
    return boiled_password
    

   def passVerify(self,rawPassword,boiledPassword):
     porridge = Porridge(self.keySecret)
     verified = porridge.verify(rawPassword,boiledPassword)
     return verified
     

        
