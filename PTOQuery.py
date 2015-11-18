import os 
import sys
import Tkinter
import tkMessageBox
import cx_Oracle 
import csv
import datetime

SQL="SELECT EMP_ID FROM TO_USERS"

#OUTPUTFILES------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#filename="C:\Users\jsnow\Desktop\HoldingTank.csv"
#entsfile="C:\Users\jsnow\Desktop\LaborTicket.csv"

f= os.path.join(os.path.expandvars("%userprofile%"),"Desktop", "HoldingTank.csv")
n= os.path.join(os.path.expandvars("%userprofile%"),"Desktop", "LaborTicket.csv")

filename= str(f);
entsfile= str(n);

FILE=open(filename, "w");

ENTSFILE=open(entsfile, "w");

outputent=csv.writer(ENTSFILE, dialect='excel')

output=csv.writer(FILE, dialect='excel')

okToPressEnter = True

#cx_oracle is a pain with env var's-------------------------------------------------------------------------------------------------------------------------------------

#os.putenv('ORACLE_HOME', '/opt/oracle/instantclient_11_2/') 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def beginSelect(event):

  global okToPressEnter 

        if okToPressEnter == False:
          pass
        else:
            okToPressEnter = False

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def HandleException(exc):
       error, = exc.args
       print >> sys.stderr, "Cant Reach Oracle:", error.code
       print >> sys.stderr, "Oracle-Error-Message:", error.message

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def csvsaved():

   tkMessageBox.showinfo("File Saved", "File Saved")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def grabDataholding():
     global date 
     global startdate
     global enddate
     connection = cx_Oracle.connect('xxxxusername', 'xxxxpassword', cx_Oracle.makedsn('x.x.x.x', 'xxxport', 'xxxSid'))   
     cursor = connection.cursor()
     startdate = e1.get()
     enddate = e2.get()
     empid = e3.get()
     if not empid:
        try: 
          cursor.execute("SELECT * FROM Table WHERE USER_ID = '%s'" % ('TIME', 'W', 'I', startdate, enddate))
          for row in cursor:
              output.writerow(row)
          cursor.close()
          connection.close()
          FILE.close()
        except cx_Oracle.DatabaseError as e:
          error = e.args
          if error.code == 1017:
             print('The credentials are incorrect for this database')
          else:
             print('Database connection error: %s'.format(e))
          raise 

     else: 
        try:
          cursor.execute() #put sql statement here 
              output.writerow(row)
          cursor.close()
          connection.close()
          FILE.close()
        except cx_Oracle.DatabaseError as e:
          error = e.args
          if error.code == 1017:
             print('The credentials are incorrect for this database')
          else:
             print('Database connection error: %s'.format(e))
          raise 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def grabEnts():
     global date 
     global startdate
     global enddate
     connection = cx_Oracle.connect('xxxxusername', 'xxxxpassword', cx_Oracle.makedsn('x.x.x.x', 'xxxport', 'xxxSid'))  
     cursor = connection.cursor()
     startdate = e1.get()
     enddate = e2.get()
     empid = e3.get()
     if not empid:
        try: 
          cursor.execute() #put sql statement here 

          for row in cursor:
              outputent.writerow(row)
          cursor.close()
          connection.close()
          ENTSFILE.close()
        except cx_Oracle.DatabaseError as e:
          error = e.args
          if error.code == 1017:
             print('The credentials are incorrect for this database')
          else:
             print('Database connection error: %s'.format(e))
          raise 

     else: 
        try:
          cursor.execute() #put sql statement here 

          for row in cursor:
              outputent.writerow(row)
          cursor.close()
          connection.close()
          ENTSFILE.close()
        except cx_Oracle.DatabaseError as e:
          error = e.args
          if error.code == 1017:
             print('The credentials are incorrect for this database')
          else:
             print('Database connection error: %s'.format(e))
          raise 


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#WINDOWCONSTUCT------------------------------------------------------------------------------------------------------------------------------------------------------------------------

     

root = Tkinter.Tk()
root.title("PTO Query")
root.geometry("500x300")

startLable = Tkinter.Label(root, text="Title", font=('Helvetica', 15))
startLable.pack()


e1 = Tkinter.Entry(root)
e2 = Tkinter.Entry(root)
e3 = Tkinter.Entry(root)
e1label = Tkinter.Label(root, text="Label 1", font=('Helvetica', 12))
e2label = Tkinter.Label(root, text="Label 2", font=('Helvetica', 12))
e3label = Tkinter.Label(root, text="Label 3", font=('Helvetica', 12))

e1.pack()
e1label.pack()
e2.pack()
e2label.pack()
e3.pack()
e3label.pack()

btnEnts = Tkinter.Button(root, text="Grab Data", command= combine_funcs(grabEnts, csvsaved))

btnEnts.pack()

btnHold = Tkinter.Button(root, text="Grab Data 2", command= combine_funcs(grabDataholding, csvsaved))

btnHold.pack()



root.bind('<Return>', beginSelect)
root.mainloop()
     
      


