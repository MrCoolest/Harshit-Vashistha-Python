# Starting code
import tkinter as Ak
from tkinter import ttk
from csv import DictWriter
import os

win = Ak.Tk()
win.title('GUI App')
# win.configure(bg='#32a2a8')

# create label

label = ttk.Label(win, text='Enter Your First name :')
label.grid(row=0, column=0, sticky=Ak.W)

label2 = ttk.Label(win, text='Enter Your Last name :')
label2.grid(row=1, column=0, sticky=Ak.W)

label3 = ttk.Label(win, text='Enter Your age :')
label3.grid(row=2, column=0, sticky=Ak.W)


label4 = ttk.Label(win, text='Enter Your E-mail id :')
label4.grid(row=3, column=0, sticky=Ak.W)

label5 = ttk.Label(win, text='Select your Gender :')
label5.grid(row=4,column=0)

# Create label
name_var = Ak.StringVar()
name_entry = ttk.Entry(win, width=16, textvariable= name_var)
name_entry.grid(row=0,column=1)
name_entry.focus()

last_var = Ak.StringVar()
last_entry = ttk.Entry(win, width=16, textvariable= last_var)
last_entry.grid(row=1,column=1)

Age_var = Ak.IntVar()
Age_entry = ttk.Entry(win, width=16, textvariable= Age_var)
Age_entry.grid(row=2,column=1)

Email_var = Ak.StringVar()
Email_entry = ttk.Entry(win, width=16, textvariable= Email_var)
Email_entry.grid(row=3,column=1)

# Creat commbobox
gender_var =Ak.StringVar()
gender_commbobox = ttk.Combobox(win, width = 13, textvariable=gender_var, state='readonly')
gender_commbobox['values'] = ('Male','Female','Other')
gender_commbobox.current(0)
gender_commbobox.grid(row=4,column=1)

# Create raidobuttton
# student, teacher
radio_var = Ak.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value='Student', variable = radio_var)
radiobtn1.grid(row=5,column=0)

radiobtn2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable = radio_var)
radiobtn2.grid(row=5,column=1)

# Create checkbutton
Check_var = Ak.IntVar()
checkbtn = ttk.Checkbutton(win, text='Check if want to Subscribe our channel', variable=Check_var)
checkbtn.grid(row=6,columnspan=3)

# # Create Button
def react():
    username = name_var.get()
    userlast = last_var.get()
    userage = Age_var.get()
    userEmail = Email_var.get()

    # print(f"Hello {username}  {userlast}, So your age is {userage} and E-mail is {userEmail}")

    userGender = gender_var.get()
    usertype = radio_var.get()
    if Check_var.get() == 0:
        subscribed = 'NO'
    else:
        subscribed = 'Yes'

    # print(userGender, usertype, subscribed)    


# just write in text files
    # with open('Entry.txt','a') as En:
    #     En.write(f"Full name = {username} {userlast}, Age = {userage}, E-mail = {userEmail}, Gender = {userGender}, he/she is {usertype}, subscribed = {subscribed} \n")


# write in csv files
    with open('User Entry.csv','a', newline='') as fw:
        fw = DictWriter(fw,fieldnames=['First name', 'Second name', 'Age', 'Email-id', 'Gender', 'User type', 'Subscribed'])
        if os.stat('User Entry.csv').st_size == 0:
            fw.writeheader()

        fw.writerow({
                'First name' : username,
                'Second name' : userlast,
                'Age' : userage,
                'Email-id' : userEmail,
                'Gender' : userGender,
                'User type' : usertype,
                'Subscribed' : subscribed 
            })

    name_entry.delete(0, Ak.END)
    last_entry.delete(0,Ak.END)
    Age_entry.delete(0, Ak.END )
    Email_entry.delete(0, Ak.END)


# label color after submit
    # label.configure(foreground='#32a2a8')
    # label2.configure(foreground='#32a2a8')
    # label3.configure(foreground='#32a2a8')
    # label4.configure(foreground='#32a2a8')
    # label5.configure(foreground='#32a2a8')
# back groun color
    # label.configure(background='#32a2a8')
    # label2.configure(background='#32a2a8')
    # label3.configure(background='#32a2a8')
    # label4.configure(background='#32a2a8')
    # label5.configure(background='#32a2a8')


Submit_button = ttk.Button(win, text='Submit', command=react)
Submit_button.grid(row=7,column=0)


win.mainloop()