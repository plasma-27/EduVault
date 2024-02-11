# from password import passFunc
# from uidGenerator import uid
# from dbConnection import *
# from signup import *



# ################## Password Functions ##################
# key="someKey"
# secret="veryVerySecret"
# rawPassword="easyPeasyPassword"
# newInstance = passFunc(key,secret,rawPassword)
# boiled_pass = newInstance.generateBoilpass()

# print(boiled_pass)
# print(len(boiled_pass))

# verified = newInstance.passVerify(rawPassword,boiled_pass)
# print(verified)

# ###########################################################



# ################  Generate UID   ####################
# aadhaarNO = "123465129837"
# uidobj = uid(aadhaarNO)
# newUid = uidobj.generate_unique_12_digit_number()
# print(newUid,len(newUid))




# dbobj = db()
# mydb, cursor = dbobj.dbconnect("credentials")
# print(mydb,cursor)

# cursor.close()
# mydb.close()

# print(mydb,cursor)    