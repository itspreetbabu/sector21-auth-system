##### Sector 21 #####



# ___________________________import module________________________________

import random
import time
import pickle
import tkinter
from tabulate import tabulate


## ___________________________ time.sleep() will slow down the loop speed  ___________________________






## _____________________________________ CONNECTIVITY CODE  ________________________________________________


import os
import mysql.connector

# For Safe DB connection
password = os.getenv("DB_PASSWORD")

if not password:
    print("Error: DB_PASSWORD not set")
    exit()

mycon = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password,
    database="auth"
)

mydb = mycon.cursor()

# _______________________________________ Starting Of the Program  ________________________________________







#######################
######################## Typing effect Code  Using "Write" function
#######################



'''   write() is used for printing texts using time module.'''
def write(sentence): 
    for words in sentence:
        print(words,end="")
        time.sleep(0.025)


'''    write_lines() is used for printing blank lines using time module.'''
def write_lines(spacing): 
    for line in range(0,lines):
        new_line="\n"
        print(new_line,end="")
        









#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
#           Fuctions Block Started
#
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



""" ag_id_check is used to check weather the agent id entered is valid or not . """

def ag_id_check(val):
    ag_id_check_exe="SELECT Agent_Id FROM authorisation"
    mydb.execute(ag_id_check_exe)
    ag_id_check_fetch=mydb.fetchall()
    ag_id_check_list=ag_id_check_fetch    

    if (val,) in ag_id_check_list:
        return True

    else:
        return False


def tt(val):
            tt_exe="SELECT * FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
            mydb.execute(tt_exe,{'Agent_Id':val})
            tt_fetch=mydb.fetchall()
            return tt_fetch



def agid_test(val):
            agid_test_exe="SELECT Agent_Id FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
            mydb.execute(agid_test_exe,{'Agent_Id':val})
            agid_test_fetch=mydb.fetchall()
            agid_test_list=agid_test_fetch[0]
            agid_test_tuple=agid_test_list[0]
            return agid_test_tuple



# admin_test function is for admin block
def admin_test(val):
            admin_test_exe="SELECT Admin_Value FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
            mydb.execute(admin_test_exe,{'Agent_Id':val})
            admin_test_fetch=mydb.fetchall()
            admin_test_list=admin_test_fetch[0]
            admin_test_tuple=admin_test_list[0]
            return admin_test_tuple

    
def admin_pass_check(val):
    passexe="SELECT Password FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(passexe,{'Agent_Id':val})
    passfetch=mydb.fetchall()
    passlist=passfetch[0]
    passtuple=passlist[0]
    return passtuple




'''    agent_password() is used for extracting password corresponding to agent id entered.'''
""" After passing security code
Asked for the Agent Id
passexe is variable holds sql query for extracting "password"
agent variable holds input of agent id
passfetch is variable holds fuction fetchall()
passlist is variable holds command to give first value of list
passtuple is variable holds command to give first value of tuple in str form"""



'''    agent_name() is used for extracting agent's name corresponding to agent id entered.'''
def agent_name(agent_name):
    agent_name_exe="SELECT Agent_Name FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_name_exe,{'Agent_Id':agent_name})
    agent_name_fetch=mydb.fetchall()
    agent_name_list=agent_name_fetch[0]
    agent_name_tuple=agent_name_list[0]
    return agent_name_tuple


def agent_age(val):
    agent_age_exe="SELECT Age FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_age_exe,{'Agent_Id':val})
    agent_age_fetch=mydb.fetchall()
    agent_age_list=agent_age_fetch[0]
    agent_age_tuple=agent_age_list[0]
    return agent_age_tuple


def agent_DOB(val):
    agent_DOB_exe="SELECT DOB FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_DOB_exe,{'Agent_Id':val})
    agent_DOB_fetch=mydb.fetchall()
    agent_DOB_list=agent_DOB_fetch[0]
    agent_DOB_tuple=agent_DOB_list[0]
    return agent_DOB_tuple


def agent_Gender(val):
    agent_Gender_exe="SELECT Gender FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_Gender_exe,{'Agent_Id':val})
    agent_Gender_fetch=mydb.fetchall()
    agent_Gender_list=agent_Gender_fetch[0]
    agent_Gender_tuple=agent_Gender_list[0]
    return agent_Gender_tuple


def agent_M_Status(val):
    agent_M_Status_exe="SELECT Marital_Status FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_M_Status_exe,{'Agent_Id':val})
    agent_M_Status_fetch=mydb.fetchall()
    agent_M_Status_list=agent_M_Status_fetch[0]
    agent_M_Status_tuple=agent_M_Status_list[0]
    return agent_M_Status_tuple



def agent_Nationality(val):
    agent_Nationality_exe="SELECT Nationality FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_Nationality_exe,{'Agent_Id':val})
    agent_Nationality_fetch=mydb.fetchall()
    agent_Nationality_list=agent_Nationality_fetch[0]
    agent_Nationality_tuple=agent_Nationality_list[0]
    return agent_Nationality_tuple


def agent_Bgroup(val):
    agent_Bgroup_exe="SELECT Blood_Group FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_Bgroup_exe,{'Agent_Id':val})
    agent_Bgroup_fetch=mydb.fetchall()
    agent_Bgroup_list=agent_Bgroup_fetch[0]
    agent_Bgroup_tuple=agent_Bgroup_list[0]
    return agent_Bgroup_tuple


def agent_EduQual(val):
    agent_EduQual_exe="SELECT Educational_Qualification FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_EduQual_exe,{'Agent_Id':val})
    agent_EduQual_fetch=mydb.fetchall()
    agent_EduQual_list=agent_EduQual_fetch[0]
    agent_EduQual_tuple=agent_EduQual_list[0]
    return agent_EduQual_tuple

def agent_passNum(val):
    agent_passNum_exe="SELECT Passport_Number FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_passNum_exe,{'Agent_Id':val})
    agent_passNum_fetch=mydb.fetchall()
    agent_passNum_list=agent_passNum_fetch[0]
    agent_passNum_tuple=agent_passNum_list[0]
    return agent_passNum_tuple

def agent_PanNum(val):
    agent_PanNum_exe="SELECT PAN_Details FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_PanNum_exe,{'Agent_Id':val})
    agent_PanNum_fetch=mydb.fetchall()
    agent_PanNum_list=agent_PanNum_fetch[0]
    agent_PanNum_tuple=agent_PanNum_list[0]
    return agent_PanNum_tuple

def agent_SID(val):
    agent_SId_exe="SELECT Specific_Identity_Proof FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_SId_exe,{'Agent_Id':val})
    agent_SId_fetch=mydb.fetchall()
    agent_SId_list=agent_SId_fetch[0]
    agent_SId_tuple=agent_SId_list[0]
    return agent_SId_tuple

def agent_ConNum(val):
    agent_ConNum_exe="SELECT Contact_Number FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_ConNum_exe,{'Agent_Id':val})
    agent_ConNum_fetch=mydb.fetchall()
    agent_ConNum_list=agent_ConNum_fetch[0]
    agent_ConNum_tuple=agent_ConNum_list[0]
    return agent_ConNum_tuple

def agent_Email(val):
    agent_Email_exe="SELECT Email_Id FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_Email_exe,{'Agent_Id':val})
    agent_Email_fetch=mydb.fetchall()
    agent_Email_list=agent_Email_fetch[0]
    agent_Email_tuple=agent_Email_list[0]
    return agent_Email_tuple


def agent_EmConNum(val):
    agent_EmConNum_exe="SELECT Emergency_Contact_Number FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(agent_EmConNum_exe,{'Agent_Id':val})
    agent_EmConNum_fetch=mydb.fetchall()
    agent_EmConNum_list=agent_EmConNum_fetch[0]
    agent_EmConNum_tuple=agent_EmConNum_list[0]
    return agent_EmConNum_tuple


def Agent_id(val):
    Agent_id_exe="SELECT Agent_Id FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(Agent_id_exe,{'Agent_Id':val})
    Agent_id_fetch=mydb.fetchall()
    Agent_id_list=Agent_id_fetch[0]
    Agent_id_tuple=Agent_id_list[0]
    return Agent_id_tuple



def agent_password(agent_pass):
    passexe="SELECT Password FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(passexe,{'Agent_Id':agent_pass})
    passfetch=mydb.fetchall()
    passlist=passfetch[0]
    passtuple=passlist[0]
    return passtuple


def Agent_status(val):
    Agent_status_exe="SELECT Agent_Status FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(Agent_status_exe,{'Agent_Id':val})
    Agent_status_fetch=mydb.fetchall()
    Agent_status_list=Agent_status_fetch[0]
    Agent_status_tuple=Agent_status_list[0]
    return Agent_status_tuple

    
def join_date(val):
    join_date_exe="SELECT Date_Of_Joining FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(join_date_exe,{'Agent_Id':val})
    join_date_fetch=mydb.fetchall()
    join_date_list=join_date_fetch[0]
    join_date_tuple=join_date_list[0]
    return join_date_tuple


def bank_name(val):
    bank_name_exe="SELECT Name_OF_Bank FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(bank_name_exe,{'Agent_Id':val})
    bank_name_fetch=mydb.fetchall()
    bank_name_list=bank_name_fetch[0]
    bank_name_tuple=bank_name_list[0]
    return bank_name_tuple


def ifsc(val):
    ifsc_exe="SELECT IFSC_Code FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(ifsc_exe,{'Agent_Id':val})
    ifsc_fetch=mydb.fetchall()
    ifsc_list=ifsc_fetch[0]
    ifsc_tuple=ifsc_list[0]
    return ifsc_tuple

def post(val):
    post_exe="SELECT POST FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(post_exe,{'Agent_Id':val})
    post_fetch=mydb.fetchall()
    post_list=post_fetch[0]
    post_tuple=post_list[0]
    return post_tuple


def Cur_loc(val):
    Cur_loc_exe="SELECT Current_Location FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(Cur_loc_exe,{'Agent_Id':val})
    Cur_loc_fetch=mydb.fetchall()
    Cur_loc_list=Cur_loc_fetch[0]
    Cur_loc_tuple=Cur_loc_list[0]
    return Cur_loc_tuple

def ope(val):
    ope_exe="SELECT Operation FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(ope_exe,{'Agent_Id':val})
    ope_fetch=mydb.fetchall()
    ope_list=ope_fetch[0]
    ope_tuple=ope_list[0]
    return ope_tuple


def training_base(val):
    training_base_exe="SELECT Training_Base FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(training_base_exe,{'Agent_Id':val})
    training_base_fetch=mydb.fetchall()
    training_base_list=training_base_fetch[0]
    training_base_tuple=training_base_list[0]
    return training_base_tuple







'''    agent_joined() is used for extracting agent's joined date corresponding to agent id entered.'''
def agent_joined(agent_joined):
    joined_exe="SELECT Joined FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(joined_exe,{'Agent_Id':agent_joined})
    joined_fetch=mydb.fetchall()
    joined_list=joined_fetch[0]
    joined_tuple=joined_list[0]
    return joined_tuple



'''    agent_account() is used for extracting agent's account number corresponding to agent id entered.'''
def agent_account_number(agent_acc):
    account_exe="SELECT Account_No FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(account_exe,{'Agent_Id':agent_acc})
    account_fetch=mydb.fetchall()
    account_list=account_fetch[0]
    account_tuple=account_list[0]
    return account_tuple



'''    agent_account_ifsc() is used for extracting agent's account's ifsc code corresponding to agent id entered.'''
def agent_account_ifsc(agent_ifsc):
    ifsc_exe="SELECT IFSC_Code FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(ifsc_exe,{'Agent_Id':agent_ifsc})
    ifsc_fetch=mydb.fetchall()
    ifsc_list=ifsc_fetch[0]
    ifsc_tuple=ifsc_list[0]
    return ifsc_tuple



'''    agent_Salary() is used for extracting agent's account balance corresponding to agent id entered.'''
def agent_salary(sal):
    balance_exe="SELECT Agent_Salary FROM authorisation WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(balance_exe,{'Agent_Id':sal})
    balance_fetch=mydb.fetchall()
    balance_list=balance_fetch[0]
    balance_tuple=balance_list[0]
    return balance_tuple



################
################
"""  Admin Manipulation Functions  """
################
################



def upd_salary():    
    print()
    write("UPDATE AGENT's SALARY ↯")
    print()
    ag_chk=1
    while ag_chk==1:  
        write("Enter Agent Id : ")
        
        ipt=input()

        adm=ipt.upper()
        if ag_id_check(adm)==True:
            ag_chk=2
            
        else:
            write("\nSorry Invalid Agent_Id ◑﹏◐ \n\t\tTry Again\n\n")
            
    print()
    write("Enter New Amount : ")
    sal=int(input())
    upd_salary_exe="UPDATE authorisation SET Agent_Salary = %(Agent_Salary)s WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(upd_salary_exe,{'Agent_Salary':sal,'Agent_Id':ipt})
    mycon.commit()
    print()
    print()
    write("Please Wait ...")
    time.sleep(0.9)
    print("\n")
    write("O_O  Desired Changes Are Saved  O_O")
    print()
    return
    
    


def upd_location():
    print()
    write("UPDATE AGENT's LOCATION ↯")
    print()
    ag_chk=1
    while ag_chk==1:  
        write("Enter Agent Id : ")
        
        ipt=input()

        adm=ipt.upper()
        if ag_id_check(adm)==True:
            ag_chk=2
            
        else:
            write("\nSorry Invalid Agent_Id ◑﹏◐ \n\t\tTry Again\n\n")

    write("Enter New Location : ")
    loc=input()
    upd_location_exe="UPDATE authorisation SET Current_Location = %(Current_Location)s WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(upd_location_exe,{'Current_Location':loc,'Agent_Id':ipt})
    mycon.commit()
    print()
    print()
    write("Please Wait ...")
    time.sleep(0.9)
    print("\n")
    write("O_O  Desired Changes Are Saved  O_O")
    print()
    return


def upd_operation():
    print()
    write("UPDATE AGENT's OPERATION ↯")
    print()
    ag_chk=1
    while ag_chk==1:  
        write("Enter Agent Id : ")
        
        ipt=input()

        adm=ipt.upper()
        if ag_id_check(adm)==True:
            ag_chk=2
            
        else:
            write("\nSorry Invalid Agent_Id ◑﹏◐ \n\t\tTry Again\n\n")

    write("Enter New Operation Name : ")
    operate=input()
    upd_operation_exe="UPDATE authorisation SET Operation = %(Operation)s WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(upd_operation_exe,{'Operation':operate,'Agent_Id':ipt})
    mycon.commit()
    print()
    print()
    write("Please Wait ...")
    time.sleep(0.9)
    print("\n")
    write("O_O  Desired Changes Are Saved  O_O")
    print()
    return



def upd_post():
    print()
    write("UPDATE AGENT's POST ↯")
    print()
    ag_chk=1
    while ag_chk==1:  
        write("Enter Agent Id : ")
        
        ipt=input()

        adm=ipt.upper()
        if ag_id_check(adm)==True:
            ag_chk=2
            
        else:
            write("\nSorry Invalid Agent_Id ◑﹏◐ \n\t\tTry Again\n\n")

    write("Enter New POST Name : ") 
    po=input()
    upd_post_exe="UPDATE authorisation SET POST = %(POST)s WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(upd_post_exe,{'POST':po,'Agent_Id':ipt})
    mycon.commit()
    print()
    print()
    write("Please Wait ...")
    time.sleep(0.9)
    print("\n")
    write("O_O  Desired Changes Are Saved  O_O")
    print()
    return


def upd_status():
    print()
    write("UPDATE AGENT's STATUS ↯")
    print()
    ag_chk=1
    while ag_chk==1:  
        write("Enter Agent Id : ")
        
        ipt=input()

        adm=ipt.upper()
        if ag_id_check(adm)==True:
            ag_chk=2
            
        else:
            write("\nSorry Invalid Agent_Id ◑﹏◐ \n\t\tTry Again\n\n")

    write("Enter Current Status : ")     
    stts=input()
    upd_status_exe="UPDATE authorisation SET Agent_Status = %(Agent_Status)s WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(upd_status_exe,{'Agent_Status':stts,'Agent_Id':ipt})
    mycon.commit()
    print()
    print()
    write("Please Wait ...")
    time.sleep(0.9)
    print("\n")
    write("O_O  Desired Changes Are Saved  O_O")
    print()
    return



def upd_adm_value():
    print()
    write("UPDATE AGENT's ADM_VALUE ↯")
    print()
    ag_chk=1
    while ag_chk==1:  
        write("Enter Agent Id : ")
        
        ipt=input()

        adm=ipt.upper()
        if ag_id_check(adm)==True:
            ag_chk=2
            
        else:
            write("\nSorry Invalid Agent_Id ◑﹏◐ \n\t\tTry Again\n\n")

    write("Enter Admin_Value : ")       
    adval=input()
    upd_adm_value_exe="UPDATE authorisation SET Admin_Value = %(Admin_Value)s WHERE Agent_Id=%(Agent_Id)s"
    mydb.execute(upd_adm_value_exe,{'Admin_Value':adval,'Agent_Id':ipt})
    mycon.commit()
    print()
    print()
    write("Please Wait ...")
    time.sleep(0.9)
    print("\n") 
    write("O_O  Desired Changes Are Saved  O_O")
    print()
    return




"""  help desk functions  """



'''    helpdesk_tk() is used for printing tk ui corresponding to agent id entered.'''

def helpdesk_tk(val):
    root=tkinter.Tk()
    root.geometry("400x400")
    tkinter.Label(root,bg="bisque",text="").pack()
    msg_acc="Account_No. = ",agent_account_number(val)
    root.configure(bg='bisque')      ########### changes color of main background color
    tkinter.Label(root,foreground="black",bg="bisque",pady=10,padx=10,font=80,text=msg_acc).pack()      ## changes the color of text background
    
    tkinter.Label(root,bg="bisque",text="").pack()
    msg_ifsc="IFSC_Code = ",agent_account_ifsc(val)
    tkinter.Label(root,foreground="black",bg="bisque",pady=10,padx=10,font=80,text=msg_ifsc).pack()
    tkinter.Label(root,bg="bisque",text="").pack()
    msg_balance="Salary = ","₹ ",agent_salary(val)      ######### new added line
    tkinter.Label(root,foreground="black",bg="bisque",pady=10,padx=10,font=80,text=msg_balance).pack()######### new added line
    root.mainloop()





'''    helpdesk_msg() is used for executing - sending message to the head quarter.'''

def helpdesk_msg():
    print()
    print()
    time.sleep(0.5)
    pmsg="Type The Message 💬 :"
    write(pmsg)
    msg_in=input(" ")
    msg_file=open("Headquter_Messages.dat","ab+")
    pickle.dump(msg_in,msg_file)
    msg_file.close()
    print()
    print()
    time.sleep(0.4)
    pmsg="Sending..."
    write(pmsg)
    time.sleep(1)
    print()
    time.sleep(0.9)
    print()
    pmsg="\t\t\t\t\t\t\t •̀ ̫ •́    Sent   •̀ ̫ •́ "
    write(pmsg)
    print()



'''   hekpdesk_adm_login()  is used for executing  - admin login block'''


def helpdesk_adm_login():
    print()
    pmsg="\t\t\t\t\t\t⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄⋄"
    write(pmsg)
    print()
    pmsg="\t\t\t\t\t\t\t   ● Admin Login ●"
    write(pmsg)
    print()
    time.sleep(0.5)

    ag_chk=1
    while ag_chk==1:  
        pmsg="Enter Your Admin Id - "
        write(pmsg)
        
        admin=input("")

        adm=admin.upper()
        if ag_id_check(adm)==True:
            ag_chk=2
            
        else:
            write("\nSorry Invalid Admin_Id ◑﹏◐ \n\t\tTry Again\n\n")
            



    
    if admin_test(admin)=="1":
        pass_chk=1
        while pass_chk==1:


        
            pmsg="Enter Password - "
            write(pmsg)
            admin_pass=int(input(""))
            
            if admin_pass==admin_pass_check(admin):
                pass_chk=2   ######### I had changed its value so that i not start the while loop of s-code
                print()
                print()
                pmsg="\n✧Data Matched ✧\n\n⨀ Welcome Sir ⨀ "
                write(pmsg)
                print()
                print()
                pmsg="\t\t\t\t\t\t\t● Admin Action Panel ●"
                write(pmsg)
                print()
                print()
                changes="1"
                while changes=="1":

                    print()
                    print()
                    pmsg="◈  To Update Salary , Press ①\n"
                    write(pmsg)
                    pmsg="◈  To Update Location , Press ②\n"
                    write(pmsg)
                    pmsg="◈  To Update Operation , Press ③\n"
                    write(pmsg)
                    pmsg="◈  To Update POST , Press ④\n" 
                    write(pmsg)
                    pmsg="◈  To Update Agent Status , Press ⑤\n"
                    write(pmsg)
                    pmsg="◈  To Update Admin Value , Press ⑥\n"
                    write(pmsg)
                    pmsg="◈  To Exit Updation Section , Press Any Other Key\n"
                    write(pmsg)
                    print()
                    print()
                    write("Required Updation Action : ")
                    adm_upd=input()
                    

                    if adm_upd=="1":
                        upd_salary()
                        write("\nTo Make More Changes Press ① \nPress Any Other Key To Exit :")
                        change=input()
                    elif adm_upd=="2":
                        upd_location()
                        write("\nTo Make More Changes Press ① \nPress Any Other Key To Exit :")
                        changes=input()
                    elif adm_upd=="3":
                        upd_operation()
                        write("\nTo Make More Changes Press ① \nPress Any Other Key To Exit :")
                        changes=input()
                    elif adm_upd=="4":
                        upd_post()
                        write("\nTo Make More Changes Press ① \nPress Any Other Key To Exit :")
                        changes=input()                        
                    elif adm_upd=="5":
                        upd_status()
                        write("\nTo Make More Changes Press ① \nPress Any Other Key To Exit :")
                        changes=input()
                        
                    elif adm_upd=="6":
                        upd_adm_value()
                        write("\nTo Make More Changes Press ① \nPress Any Other Key To Exit :")
                        changes=input()
                        
                    else:
                        write("\n\n")
                        changes="z"


            else:
                pmsg="\nInvalid Admin Password \n\t\tTry Again\n\n"
                write(pmsg)


"""  admin block finished   """



def helpdesk_sw_ac():
    write("\nLogging Out \n")
    time.sleep(1)
    global condition
    condition=2
    





def helpdesk_disconnect():
    print("\n"*2)
    time.sleep(1)
    pmsg="Disconnecting From Server ..."
    write(pmsg)
    time.sleep(1.4)
    print()
    time.sleep(0.3)
    pmsg="\t\t\t\t\t\t\t  *_* Disconnected *_*"
    write(pmsg)
    time.sleep(0.3)
    print()
    time.sleep(0.3)
    print()
    time.sleep(0.3)
    print()
    time.sleep(0.3)
    pmsg="\t\t\t\t\t   | O_O Thank You For Giving Time To My Program O_O |"
    write(pmsg)
    time.sleep(0.3)
    print()
    time.sleep(0.3)
    pmsg="\t\t\t\t\t\t\t    | Priyam Singh |"
    write(pmsg)
    time.sleep(0.3)
    print()
    time.sleep(0.3)
    global chk   ############ i had make ckh as global and changed its value so that i not start the while loop of s-code
    chk=2
    return False
    


def per_action(val):
    if ope_in=="1":
        helpdesk_tk(agent)
        
    elif ope_in=="2":
        helpdesk_msg()


    elif ope_in=="3":                    
        helpdesk_disconnect()

        return False

        
    else:
        True        






#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
#           Fuctions Block Ended
#
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



pmsg="|  Hello  |"
write(pmsg)

print()
time.sleep(0.4)
print() 

#^^^^^^^^^^^^^^^^^  Welcome to Sector 21   ^^^^^^^^^^^^^^^^^

pmsg="|  Welcome To Sector 21  |"
write(pmsg)


print()
time.sleep(0.07)
print()



#______________________________________    recaptcha code ______________________________________

#______________________________rd is variable for holding random value ______________________________________
#______________________________rdstr converts the int value to str  ______________________________________
#______________________________lrdstr hold the length of rdstr ______________________________________
#______________________________orival the actual value of capthca ______________________________________
#______________________________rd is variable for holding random value ______________________________________



rd=random.randint(100000000,999999999)

rdstr=str(rd)
lrdstr=len(rdstr)
orival=rdstr[(lrdstr-2)]


pmsg="DiGi Code : "
write(pmsg)
pmsg=rdstr
write(pmsg)


print()
time.sleep(0.07)
print() 

# ______________________________________  recaptcha input  ______________________________________
# _______________________ orivalin is variable for holding recaptcha input ______________________________________


pmsg="Enter Passcode :"
write(pmsg)
orivalin=input(" ")



# ______________________________________ condition of passing recaptcha ______________________________________

# __________________________ matching the recaptcha generated and the value entered ______________________________________

if orivalin==orival:
    print()
    print()
    time.sleep(0.7)



#^^^^^^^^^^^^^^^^^  Passed  ^^^^^^^^^^^^^^^^^


    pmsg="✧ Passed ✧"
    write(pmsg)

    print()
    time.sleep(0.07)
    print()
  



# __________________________ asked for the security code i.e., captcha number 2 _________________________________

# ____________________ cap2 is variable that holds the security code value i.e., awr420____________________________________





    chk=1
    while chk==1:
        print()
        pmsg="S-Code :"
        write(pmsg)
        cap2=str(input(""))
        time.sleep(0.07)
        print()


        S_CODE = "awr420"

        if cap2== S_CODE:


#^^^^^^^^^^^^^^^^^  Matched  ^^^^^^^^^^^^^^^^^
            time.sleep(0.07)
            pmsg="✧ Matched ✧"
            write(pmsg)

            print()
            time.sleep(0.07)
            print()



            ag_chk=1
            while ag_chk==1:
                
                pmsg="Enter Agent Id :"
                write(pmsg)
              
                agent_cap=input(" ")
                agent=agent_cap.upper()
                if ag_id_check(agent)==True:
                    ag_chk=2
                    
                else:
                    write("\nSorry Invalid Agent_Id ◑﹏◐ \n\t\tTry Again\n\n")
                    


        
### ........................................ Password matching block ........................................###



# _____________________________ pass_in ______________________________________


            pmsg="Enter Password  :"
            write(pmsg)
            
            try:
                 pass_in = int(input(""))

            except:
                print("Invalid Password !!!")
                continue
            if pass_in==agent_password(agent):




### ........................................ Password matching block finished........................................###





                
               
                time.sleep(0.5)
                print()
                time.sleep(0.3)
                
                pmsg="\t\tConnecting To The Server ..."
                write(pmsg)
                
                print()
                time.sleep(1)
                
                pmsg="\t\tChecking data entered"
                write(pmsg)

                print()
                time.sleep(1.5)
                print()

                pmsg="✧ Data Matched ✧"
                write(pmsg)      
                print()
                time.sleep(1.2)

                lines=14
                write_lines(lines)
                


############################################## this is user data section ############################################

                
                            
                time.sleep(0.7)
                print()                
         
# _____________________________ agent data section starts here______________________________________
          
                              
                ttt=tt(agent)
                
                print(tabulate(ttt,headers=["Agent_Name","Age","DOB","Gender","Marital Status","Nationality","Blood_Group","Educational_Qualification","Passport_Number","Pan_Details","Specific_Identity_Proof","Contact_Number","Email_Id","Emergency_Contact_Number","Agent_Id","Password","Agent_Status","Date_Of_Joining","Name_Of_Bank","Account_No","IFSC_Code","Agent_Salary","Post","Current_Location","Operation","Training_Base"],tablefmt="outline"))




        

# _____________________________ agent data section ended here______________________________________



                lines=14
                write_lines(lines)


# _____________________________ HelpDesk block asking for required action ______________________________________




                condition=1
                while condition==1:
                    print()
                    print()
                    pmsg="\t\t\t\t\t\t-----------------------------------"
                    write(pmsg)
                    print()
                    pmsg="\t\t\t\t\t\t\t    ● HelpDesk ●"
                    write(pmsg)
                    print()
                    time.sleep(0.5)

                    
                    write("◈  For Bank Details , Press  ① \n")
                    write("◈  To Message To Headquater , Press ② \n")
                    write("◈  Admin Login , Press ③ \n")
                    write("◈ To Switch Account , Press ④ \n")  ####### New Option To Switch Accounts so that no need to reopen the code.
                    write("◈  To Dissconnect Server , Press ⑤ ") 
                    time.sleep(0.4)
                    print()
                    time.sleep(0.4)
                    print()
                  
                    pmsg="Required Action : "
                    write(pmsg)
                    ope_in=input(" ")

                    if ope_in=="1":
                        helpdesk_tk(agent)

                    elif ope_in=="2":
                        helpdesk_msg()


                    elif ope_in=="3":
                        helpdesk_adm_login()

                    elif ope_in=="4":
                        helpdesk_sw_ac()
                        



                    elif ope_in=="5":
                        pmsg="Press ①, And Then Enter To Confirm\n To Escape Press Any Other Key "
                        write(pmsg)
                        dis=input(" : ")
                        if dis=="1":
                            
                            helpdesk_disconnect()
                            break
                        else:
                            pmsg="\nAborting Connection Break-Down ..."
                            write(pmsg)
                            write_lines(1)
                            continue

                       
                    else:
                        pmsg="Invalid !!! \n"
                        write(pmsg)
                        
                        False

            else:
                time.sleep(0.5)
                print()
                time.sleep(0.3)
                
                pmsg="\t\tConnecting To The Server ..."
                write(pmsg)
                
                print()
                time.sleep(1)
                
                pmsg="\t\tChecking data entered"
                write(pmsg)

                print()
                time.sleep(1.5)
                print()

                pmsg="° Sorry Invalid Entry !!! ° \n° Data Not Matched !!! °"
                write(pmsg)      
                print()
                time.sleep(1.2)
                

               

        else:
            print()
            pmsg="Sorry Invalid S-Code ◑﹏◐ \n\t\tTry Again "
            write(pmsg)
            False
            

 


else:
    print()
    print()
    pmsg="Sorry Invalid Digi-Code ◑﹏◐ "
    write(pmsg)


 
mydb.close()
mycon.close()
