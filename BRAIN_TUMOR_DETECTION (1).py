#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import cv2
import numpy as np
from keras.preprocessing import image
import warnings
warnings.filterwarnings("ignore")
from keras.preprocessing.image import load_img, img_to_array 
from keras.models import  load_model
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


model = load_model("best_model (1).h5")


# In[3]:


import keras.utils as image
import tensorflow as tf
from keras.preprocessing import image


# In[4]:


import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",database="project2")
if mycon.is_connected():
    print("Successfully connected to MySQL Database")


# In[6]:


cursor=mycon.cursor()
cursor.execute("use project2")


# In[ ]:



import tkinter#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
root = Tk()
root.geometry("700x500")
root.config(bg='black')
root.title("CLASSIFY.com")
def form():
    name=e1.get()
    gender=e2.get()
    age=e3.get()
    if (name=="" and gender=="" and age==""):
        messagebox.showinfo("","Blank Not Allowed")
    else:
        messagebox.showinfo("","DETAILS SAVED")
        cursor.execute(f"insert into form(U_name,U_gender,U_age) values('{e1.get()}','{e2.get()}','{e3.get()}')")
        mycon.commit()
def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((350,350)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =Button(root,image=img) # using Button 
    b2.place(x=240,y=150)
    
def call_model():
    path="Not-Cancer-_1_.png"
    #path="Cancer (1).png"
    img1=image.load_img(path,target_size=(224,224),)
    i=image.img_to_array(img1)/255
    input_arr=np.array([i])
    input_arr.shape
    #pred=model.predict_classes(input_arr)[0][0]
    pred = (model.predict(input_arr) > 0.5).astype("int32")
    if pred==0:
        print("THE MRI IMAGE IS OF BRAIN TUMOR")
        #l = Label(root, text = "THE MRI IMAGE IS OF BRAIN TUMOR")
        #l.config(font =("Courier", 14))
        #l.pack()
        Label(root, text=" THE MRI IMAGE IS OF BRAIN TUMOR", bg="yellow", fg="black").place(x=300, y=700)
    else:
        print("The MRI IMAGE IS OF HEALTHY BRAIN ")
        #l1 = Label(root, text = "THE MRI IMAGE IS OF HEALTHY BRAIN")
        #l1.config(font =("Courier", 14))
        #l1.pack()
        Label(root, text="The MRI IMAGE IS OF HEALTHY BRAIN ", bg="yellow", fg="black").place(x=300, y=700)
Label(root, text=" WELCOME TO BRAIN TUMOR CLASSIFIER", bg="black", fg="white",font=('Times', 24)).place(x=550, y=0)
Label(root,text="PLEASE FILL UP THE FORM FIRST",bg="black",fg="white",font=('Times',14)).place(x=750,y=100)
global e1 
global e2
global e3

Label(root,text="NAME",bg="black",fg="white").place(x=750,y=160)
Label(root,text="GENDER",bg="black",fg="white").place(x=750,y=200)
Label(root,text="AGE",bg="black",fg="white").place(x=750,y=240)
e1=Entry(root,bd=5)
e1.place(x=850,y=160)
e2=Entry(root,bd=5)
e2.place(x=850,y=200)
e3=Entry(root,bd=5)
e3.place(x=850,y=240)
Button(root,text="Submit",command=form,height=3,width=13,bd=6,bg="white",fg="black").place(x=850,y=300)
b1 = Button(root, text='Upload File', width=20,bg="white",font=80,command = lambda:upload_file())
b1.place(x=300, y=100)
b3=Button(root,text="Predict",width=15,bg="green",fg="white",font=80,command=call_model)
b3.place(x=320,y=600)
root.mainloop()


# In[ ]:





# In[ ]:




