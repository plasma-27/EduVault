from password import passFunc
from uidGenerator import uid



################## Password Functions ##################
key="someKey"
secret="veryVerySecret"
rawPassword="easyPeasyPassword"
newInstance = passFunc(key,secret,rawPassword)
boiled_pass = newInstance.generateBoilpass()

print(boiled_pass)
print(len(boiled_pass))

verified = newInstance.passVerify(rawPassword,boiled_pass)
print(verified)

###########################################################



################  Generate UID   ####################
aadhaarNO = "123465129837"
uidobj = uid(aadhaarNO)
newUid = uidobj.generate_unique_12_digit_number()
print(newUid,len(newUid))
