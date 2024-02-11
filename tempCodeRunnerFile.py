from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
import mysql.connector
import hashlib
import random
from password import passFunc
from uidGenerator import uid
from dbConnection import *
from signup import *

def saveinfo():
    # Get all the user inputs
    full_name = e1.get()
    email = e2.get()
    dob_value = dob.get()
    gender = "Male" if var.get() == 1 else "Female"
    contact_no = e3.get()
    aadhaar_no = e4.get()
    password = e5.get()
    
    uidobj = uid(aadhaar_no)
    generated_uid = uidobj.generate_unique_12_digit_number()
    
    passFuncobj = passFunc("key",password,password)
    boiledPass = passFuncobj.generateBoilpass()
    
    studentInsert(generated_uid,full_name, email, dob_value, gender, contact_no, aadhaar_no, boiledPass)
    