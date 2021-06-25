from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Automeet by Chandan")
window.configure(background="Black")
window.geometry('310x250')
window.resizable(False, False)

#messagebox.showinfo('Message title','Message content')
lbl = Label(window, text="Gmeet ID: ", font=("Arial Bold", 10), fg="White", bg="Black")
lbl.grid(column=0, row=0,pady=5,padx=10, sticky=W)
meetcode = Entry(window,width=20)
meetcode.grid(column=1, row=0, pady=10, sticky=W)
meetcode.focus()

lbl = Label(window, text="Message: ", font=("Arial Bold", 10), fg="White", bg="Black")
lbl.grid(column=0, row=1, sticky=W,padx=10)
message = Entry(window,width=20)
message.grid(column=1, row=1, pady=10, sticky=W)

lbl = Label(window, text="Keyword: ", font=("Arial Bold", 10), fg="White", bg="Black")
lbl.grid(column=0, row=2, sticky=W,padx=10)
keyword = Entry(window,width=20)
keyword.grid(column=1, row=2, pady=10, sticky=W)

lbl = Label(window, text="Time Gap:  ", font=("Arial Bold", 10), fg="White", bg="Black")
lbl.grid(column=0, row=3, sticky=W,padx=10)
timeGap = Entry(window,width=20)
timeGap.grid(column=1, row=3, pady=10, sticky=W)

rad1 = Radiobutton(window,text='Only Join Meet', value=1,bg="black",fg="Green", font=("Arial Bold", 10)).grid(column=0, row=4, sticky=W,padx=5)

rad2 = Radiobutton(window,text='Mark Attendence', value=2,bg="black",fg="Green", font=("Arial Bold", 10)).grid(column=0, row=5, sticky=W,padx=5)

rad3 = Radiobutton(window,text='Recognize Keyword', value=3,bg="black",fg="Green", font=("Arial Bold", 10)).grid(column=0, row=6, sticky=W,padx=5)

def submit(meetcode,message,keyword,timeGap):
    print('clicked')
    meetcode= meetcode.get()
    message = message.get()
    keyword = keyword.get()
    timeGap = timeGap.get()
    print(timeGap)

btn = Button(window, text="SUBMIT", font=("Arial Bold", 10), bg="green", fg="White",width=14,command=submit(meetcode,message,keyword,timeGap))

btn.grid(column=1, row=5)

window.mainloop()