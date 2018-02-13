"""
########StudentProgram#######
1. Show all students information.
2. Insert a student information.
3. Delete a student information.
4. Modify a student information.
5. Exit.
##############################
select number: 


#1
-----------------------------------------------------
No.  | Name | StudentID | Age | Gender | Grade | GPA 
1.     sean   13143333    26     male      4     4.0
2. ...
3. ...
-----------------------------------------------------

Enter 'q' return to main menu
:


#2
Press Enter to register information(* If exit, Enter 'q')
----------------------------
Name : 
StudentID : 
Age :
Gender :
Grade :
GPA :
----------------------------


#3
Enter the studentID to delete(* If exit, Enter 'q')
:

success!!

Not found studentID!

#4
Enter the studenttID to modify(* If exit, Enter 'q') 
:

Name : 
StudentID : 
Age : 
Gender : 
Grade : 
GPA : 

success!!

Not found studentID!

"""


class mainMenu:
  def __init__(self):
    c = Console.getconsole()
c.text(0, -1, 'And this is the string at the bottom of the console')
