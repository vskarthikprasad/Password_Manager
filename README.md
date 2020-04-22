It is a simple password manager where one can store their important login details with the host name.



I have used mysql for this task.




First you need to create one database. Inside that create a table for storing your master password.Here i have created a master table with name and passsword columns

Input you password details throught mysql.
After that create another table for storing all the login details. This tabkle should have 3 columns host,username,password.
After crreating these two tables , one has to link them with your python file.
Then i have create forms with tkinter package.
