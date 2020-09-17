from tkinter import * # Filedialog helps us pick the apps, Text to display text
import os # allows us to run the apps that we are gonna add to the mother app
import xlrd

root=Tk()
root.title("FAFSA Version")
root.geometry("700x700")
def file():

    wb = xlrd.open_workbook("testfile.xlsx")
    sheet = wb.sheet_by_index(0)
    # print("Hello",mytextbox1.get())
    sheet.cell_value(0, 0)

    label1=Label(root,text="Last_name: " + mytextbox1.get())
    label1.grid(row=2,column=0)
    label2=Label(root,text="First_name: " + mytextbox2.get())
    label2.grid(row=2,column=1)
    for i in range(sheet.nrows):
        if sheet.cell_value(i,0)==mytextbox1.get():
            if sheet.cell_value(i,1)==mytextbox2.get():
                print(sheet.row_values(i,0))
                contact_no=str(sheet.cell_value(i,2))
                # Label3=Label(root,text=sheet.cell_value(i,2))
                Label3=Label(root,text="Contact_no:  "+contact_no)
                Label3.grid(row=2,column=2)
                Label4=Label(root,text="Email: "+sheet.cell_value(i,3))
                Label4.grid(row=2,column=3)




mylabel = Label(root,text="Enter the Last Name:").grid(row=0,column=0)
# mylabel.insert(0,"Enter Your Last Name")
mytextbox1= Entry(root,width=30)
mytextbox1.grid(row=1,column=0)

mylabel1 = Label(root,text="Enter the First Name:").grid(row=0,column=1)



mytextbox2= Entry(root,width=30 )
mytextbox2.grid(row=1,column=1)


myButton=Button(root,text="Submit",bg="yellow", command=file)
myButton.grid(row=1,column=2)


root.mainloop()
