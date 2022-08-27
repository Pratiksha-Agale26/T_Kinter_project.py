from cgitb import text  #CGI stands for Common Gateway Interface in Python which is a set 
                        # of standards that explains how information or data is 
                          #exchanged between the web server and a routine script.

from tkinter import *   #Tkinter is the standard GUI library for Python.
                         #Python when combined with Tkinter provides a fast and easy way
                         #  to create GUI applications.

root = Tk()              #tk() helps to display the root window and 
                        #manages all the other components of the tkinter application.

root.title("CHATBOT")
# root.geometry("500x500")

# e=Entry(root,width=100)
e= Entry(root,width = 100,fg = "blue")
e.grid(row=9,column=8)  #The grid() geometry manager organises widgets in a table-like structure in the parent widget.

def send():
    send="YOU :"+ e.get() #The get() method returns the value of the item with the specified key.
    text.insert(END,"\n"+send)  # END for stabling of curssor
    if (e.get()=="hello"):
        text.insert(END,"\n"+"Bestie :hii")
    elif (e.get()=="hii"):
        text.insert(END,"\n"+"Bestie :Hello")
    elif (e.get()=="how are you"):
        text.insert(END,"\n"+"Bestie :fine and you")
    elif (e.get()=="yes,i'm also fine"):
        text.insert(END,"\n"+"Bestie :nice to hear")
    elif (e.get()=="i miss you a lots"):
        text.insert(END,"\n"+"Bsetie :i also")
    else:
        text.insert(END,"\n"+"Bestie :sorry i didn't get it")
    e.delete(0,END)

text=Text(root)  # App(root) is to make an instance with your class,
                 # which then has access to your root window.
text.grid(row=0,column=0,columnspan=2)
# e=Entry(root,width=100)
Button(root,text="send",command=send,bg="light blue").grid(row=1,column=1)
e.grid(row=1,column=0)
# root.title("CHATBOT")
root.mainloop() #mainloop() tells Python to run the Tkinter event loop.