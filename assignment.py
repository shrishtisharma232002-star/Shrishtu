import mysql.connector


# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shrishti"
# )
# raha=mydb.cursor()
# raha.execute("create database db7")
# mydb.commit()
# raha.close()
# print("done")



# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shrishti",
#     database="db7"
# )

# raha=mydb.cursor()
# s="create table students(id int, name varchar(50),age int,grade varchar(50),city varchar(50))"
# raha.execute(s)
# mydb.commit()
# raha.close()
# print("baby")



# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shrishti",
#     database="db7"
# )

# raha=mydb.cursor()
# s="insert into students(id,name,age,grade,city)values(%s,%s,%s,%s,%s)"
# i=input("Enter id:")
# c=input("Enter name:")
# d=input("Enter age:")
# e=input("Enter grade:")
# f=input("Enter city:")

# value=(i,c,d,e,f)
# raha.execute(s,value)
# mydb.commit()
# raha.close()
# print("baby")


# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shrishti",
#     database="db7"
# )

# raha=mydb.cursor()
# s="select * from students"
# raha.execute(s)
# result=raha.fetchall()
# print(result)
# mydb.commit()
# raha.close()
# print("baby")




# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shrishti",
#     database="db7"
# )
# cursor=mydb.cursor()
# a="update students set city=%s where id=%s"
# value=("Banglore",23)
# cursor.execute(a,value)
# mydb.commit()
# cursor.close()
# print("done")



# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shrishti",
#     database="db7"
# )
# cursor=mydb.cursor()
# a="update students set age=age+1 where grade='B'"
# cursor.execute(a)
# mydb.commit()
# cursor.close()
# print("done")


# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shrishti",
#     database="db7"
# )
# cursor=mydb.cursor()
# a="update students set grade='A' where age>20"
# cursor.execute(a)
# mydb.commit()
# cursor.close()
# print("done")



# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="shrishti",
#     database="db7"
# )
# cursor=mydb.cursor()
# a="delete from students where age<20"
# cursor.execute(a)
# mydb.commit()
# cursor.close()
# print("done")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="shrishti",
    database="db7"
)
cursor=mydb.cursor()
a="delete from students where age>20"
cursor.execute(a)
mydb.commit()
cursor.close()
print("done")