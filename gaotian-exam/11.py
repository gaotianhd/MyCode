#! usr/bin/python
#coding:utf-8

import pymongo
import sys

host = sys.argv[1]
port = 27017

client = pymongo.MongoClient(host,port)
print "connect ok!"

db = client.stu
print "connect stu ok!"

coll = db.first
print "connect first ok!"

# def insert_one(insertstr):
#     # insert one doc
#     result = coll.insert_one({insertstr})
#     print result
#     print result.inserted_id
def insert_one(str1,name,age,hobby):
    newhobby = hobby.split(",")
    infor = {
    "name":"",
    "age":0,
    "hobby":[]
    }
    infor["name"] = name
    infor["age"] = int(age)
    infor["hobby"] = newhobby
    coll.insert_one(infor)

def find_name(name):
    findname = {
    "name":"",
    }
    findname["name"] = name
    cursor = coll.find(findname)
    for ret in cursor:
        print ret
def find_age(age):
    findage = {
    "age":"",
    }
    findage["age"] = int(age)
    cursor = coll.find(findage)
    for ret in cursor:
        print ret

def delete_name(name):
    deletename = {
    "name":"",
    }
    deletename["name"] = name
    result = coll.delete_many(deletename)
    if(result.deleted_count > 0):
        print "删除成功！"
    else:
        print "【没有符合条件！】"
def delete_age(age):
    deleteage = {
    "age":"",
    }
    deleteage["age"] = int(age)
    result = coll.delete_many(deleteage)
    if(result.deleted_count > 0):
        print "删除成功！"
    else:
        print "【没有符合条件！】"

def update_name(name):
    name1 = {
    "name":""
    }
    name1["name"] = name
    up_name = raw_input(">>>请输入要改成的名字：")
    up_age = raw_input(">>>请输入要改成的年龄：")
    up_hobby = raw_input(">>>请输入要改成的爱好(多个爱好逗号隔开)：")

    if(up_name != ""):
        up_name1 = {
        "$set":{
        "name":""
        }
        }
        up_name1["$set"]["name"] = up_name
        coll.update_many(name1,up_name1)
        print "【姓名修改成功！】"

    if(up_age != ""):
        up_age1 = {
        "$set":{
        "age":""
        }
        }
        up_age1["$set"]["age"] = int(up_age)
        coll.update_many(name1,up_age1)
        print "【年龄修改成功！】"

    if(up_hobby != ""):
        up_hobby1 = {
        "$set":{
        "hobby":[]
        }
        }
        up_hobby2 = up_hobby.split(",")
        up_hobby1["$set"]["hobby"] = up_hobby2
        coll.update_many(name1,up_hobby1)
        print "【爱好修改成功！】"

def update_age(age):
    age1 = {
    "age":""
    }
    age1["age"] = int(age)
    up_name = raw_input(">>>请输入要改成的名字：")
    up_age = raw_input(">>>请输入要改成的年龄：")
    up_hobby = raw_input(">>>请输入要改成的爱好(多个爱好逗号隔开)：")

    if(up_name != ""):
        up_name1 = {
        "$set":{
        "name":""
        }
        }
        up_name1["$set"]["name"] = up_name
        coll.update_many(age1,up_name1)
        print "【姓名修改成功！】"

    if(up_age != ""):
        up_age1 = {
        "$set":{
        "age":""
        }
        }
        up_age1["$set"]["age"] = int(up_age)
        coll.update_many(age1,up_age1)
        print "【年龄修改成功！】"

    if(up_hobby != ""):
        up_hobby1 = {
        "$set":{
        "hobby":[]
        }
        }
        up_hobby2 = up_hobby.split(",")
        up_hobby1["$set"]["hobby"] = up_hobby2
        coll.update_many(age1,up_hobby1)
        print "【爱好修改成功！】"

while True:
    print "1.insert"
    print "2.find"
    print "3.update"
    print "4.delete"
    print "5.exit"
    op = raw_input(">>>请输入要操作的数字:")
    if(op == "1"):
        while True:
            str1 = raw_input(">>>输出##退出,输入其他继续：")
            if(str1 == "##"):
                break
            name = raw_input(">>>请输入姓名：")
            age = raw_input(">>>请输入年龄：")
            hobby = raw_input(">>>请输入爱好(多个爱好以逗号隔开)：")
            if(name != "" and age != ""):
                insert_one(str1,name,age,hobby)
            else:
                print "【姓名年龄不能为空！】"
    if(op == "2"):
        while True:
            print "1.按姓名查找"
            print "2.按年龄查找"
            print "3.退出"
            op1 = raw_input(">>>请输入查找方式:")
            if(op1 == "1"):
                while True:
                    print "【按姓名查找】"
                    str1 = raw_input(">>>输出##退出,输入其他继续：")
                    if(str1 == "##"):
                        break
                    findname = raw_input(">>>请输入姓名：")
                    if(findname == ""):
                        print "【姓名不能为空！】"
                    else:
                        print "11111"
                        find_name(findname)
            if(op1 == "2"):
                while True:
                    print "【按年龄查找】"
                    str1 = raw_input(">>>输出##退出,输入其他继续：")
                    if(str1 == "##"):
                        break
                    findage = raw_input(">>>请输入年龄：")
                    if(findage == ""):
                        print "【年龄不能为空！】"
                    else:
                        find_age(findage)
            if(op1 == "3"):
                break
    if(op == "3"):
        while True:
            print "1.按姓名修改"
            print "2.按年龄修改"
            print "3.退出"
            op1 = raw_input(">>>请输入修改方式:")
            if(op1 == "1"):
                while True:
                    print "【按姓名修改】"
                    str1 = raw_input(">>>输出##退出,输入其他继续：")
                    if(str1 == "##"):
                        break
                    updatename = raw_input(">>>请输入姓名：")
                    if(updatename == ""):
                        print "【姓名不能为空！】"
                    else:
                        update_name(updatename)
            if(op1 == "2"):
                while True:
                    print "【按年龄修改】"
                    str1 = raw_input(">>>输出##退出,输入其他继续：")
                    if(str1 == "##"):
                        break
                    updateage = raw_input(">>>请输入年龄：")
                    if(updateage == ""):
                        print "【年龄不能为空！】"
                    else:
                        update_age(updateage)
            if(op1 == "3"):
                break
    if(op == "4"):
        while True:
            print "1.按姓名删除"
            print "2.按年龄删除"
            print "3.退出"
            op1 = raw_input(">>>请输入删除方式:")
            if(op1 == "1"):
                while True:
                    print "【按姓名删除】"
                    str1 = raw_input(">>>输出##退出,输入其他继续：")
                    if(str1 == "##"):
                        break
                    findname = raw_input(">>>请输入姓名：")
                    if(findname == ""):
                        print "【姓名不能为空！】"
                    else:
                        delete_name(findname)
            if(op1 == "2"):
                while True:
                    print "【按年龄删除】"
                    str1 = raw_input(">>>输出##退出,输入其他继续：")
                    if(str1 == "##"):
                        break
                    findage = raw_input(">>>请输入年龄：")
                    if(findage == ""):
                        print "【年龄不能为空！】"
                    else:
                        delete_age(findage)
            if(op1 == "3"):
                break
    if(op == "5"):
        break
