from django.shortcuts import render, redirect
import time
from django.http import JsonResponse, HttpResponseRedirect
import sqlite3
from nanoid import generate
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    return render(request, "xiaotieba/index.html")


def mine(request):
    return render(request, "xiaotieba/mine.html")


def follow(request):
    return render(request, "xiaotieba/follow.html")


def member(request):
    return render(request, "xiaotieba/member.html")


def collection(request):
    return render(request, "xiaotieba/collection.html")


def history(request):
    return render(request, "xiaotieba/history.html")


def posts(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    data = getRowFromContentTable(start, end+1)
    for i in data:
        print(i)
    # Generate list of posts
    # data = []
    # for i in range(start, end + 1):
    #     data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(0.5)
    # Return list of posts
    return JsonResponse({
        "posts": data
    })


def login(request):
    error = request.GET.get('error') or ''
    return render(request, "xiaotieba/login.html", {
        'error': error
    })


def register(request):
    return render(request, "xiaotieba/register.html")

# 如果数据库不存在就创建数据库，如果存在就正常插入数据，username不能重复
# 因为数据库经常出现问题，所以使用很多try-except结构


def operateInsertUserTable(id, username, password, cookie):
    conn = sqlite3.connect('user.db')
    print("open successfully")
    c = conn.cursor()
    # if the doesn't exit,create it
    try:
        create_table_sql = """CREATE TABLE USERLOGIN
                        (ID TEXT PRIMARY KEY  NOT NULL,
                        USERNAME   TEXT   NOT NULL   UNIQUE,
                        PASSWORD   TEXT   NOT NULL,
                        COOKIE     TEXT   NOT NULL   UNIQUE);"""
        c.execute(create_table_sql)
    except:
        # if exits,print error
        print("Create table failed")
    # insert data
    try:
        c.execute(
            f"INSERT INTO USERLOGIN (ID,USERNAME,PASSWORD,COOKIE) VALUES ('{id}', '{username}', '{password}','{cookie}' )")
    except:
        print("insert table failed and maybe username repeated")
        return
    else:
        print("insert table successfully")
        conn.commit()
    finally:
        conn.close()

# 这个函数返回三种状态:
# 0:登录成功 1:查找不到该用户名 2.用户输入密码错误


def operateVerifyUserTable(username, password):
    cursorUsername = ''
    cursorPassword = ''
    conn = sqlite3.connect('user.db')
    print("open successfully")
    c = conn.cursor()
    cursor = c.execute(
        f"SELECT username,password  from USERLOGIN where username = '{username}'")
    for row in cursor:
        cursorUsername = row[0]
        cursorPassword = row[1]
    conn.close()
    if (cursorUsername == ''):
        print('查找不到该用户名')
        return 1
    else:
        if (cursorPassword == password):
            print('登录成功')
            return 0
        else:
            print('用户输入密码错误')
            return 2


def operateInsertContentTable(id, username, content, time):
    conn = sqlite3.connect('user.db')
    print("open successfully")
    c = conn.cursor()
    # if the doesn't exit,create it
    try:
        create_table_sql = """CREATE TABLE CONTENT
                        (ID TEXT PRIMARY KEY  NOT NULL,
                        USERNAME  TEXT   NOT NULL,
                        CONTENT   TEXT   NOT NULL
                        TIME      INTEGER   NOT NULL);"""
        c.execute(create_table_sql)
    except:
        # if exits,print error
        print("Create table failed")
    # insert data
    try:
        c.execute(
            f"INSERT INTO CONTENT (ID,USERNAME,CONTENT,TIME) VALUES ('{id}', '{username}', '{content}','{time}' )")
    except:
        print("insert table failed")
    else:
        print("insert table successfully")
        conn.commit()
    finally:
        conn.close()


def getRowFromContentTable(start, end):
    data = []
    conn = sqlite3.connect('user.db')
    print("open successfully")
    c = conn.cursor()
    cursor = c.execute(
        f"SELECT username,content,time FROM content WHERE rowid <= {end} and rowid >={start};")
    for row in cursor:
        post = {
            'name': "",
            'appendwords': "",
            'time': ""
        }
        post["name"] = row[0]
        post["appendwords"] = row[1]
        post["time"] = row[2]
        data.append(post)
    conn.close()
    return data


def getSpecificRowFromContentTable(start, end, keywords):
    data = []
    conn = sqlite3.connect('user.db')
    print("open successfully")
    c = conn.cursor()
    cursor = c.execute(
        f"SELECT username,content,time FROM content WHERE rowid <= {end} and rowid >={start} and content like '%{keywords}%';")
    for row in cursor:
        post = {
            'name': "",
            'appendwords': "",
            'time': ""
        }
        post["name"] = row[0]
        post["appendwords"] = row[1]
        post["time"] = row[2]
        data.append(post)
    conn.close()
    return data


def operateUserTable_getCookie(username):
    conn = sqlite3.connect('user.db')
    print("open successfully")
    c = conn.cursor()
    cursor = c.execute(
        f"SELECT cookie  from USERLOGIN where username = '{username}'")
    for row in cursor:
        cookie = row[0]
    conn.close()
    return cookie


def operateUserTable_getUsername(cookie):
    conn = sqlite3.connect('user.db')
    print("open successfully")
    c = conn.cursor()
    cursor = c.execute(
        f"SELECT username  from USERLOGIN where cookie = '{cookie}'")
    for row in cursor:
        username = row[0]
    conn.close()
    return username


def loginWork(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    verifyResult = operateVerifyUserTable(username, password)
    # 登录成功
    if (verifyResult == 0):
        cookie = operateUserTable_getCookie(username)
        response = HttpResponseRedirect('/xiaotieba/')
        response.set_cookie(
            'cookie', cookie, expires=datetime.now()+timedelta(days=14))
        response.set_cookie('username', username,
                            expires=datetime.now()+timedelta(days=14))
        return response
    # 查找不到该用户名
    elif (verifyResult == 1):
        return HttpResponseRedirect('/?error=查找不到该用户名')
    # 用户输入密码错误
    else:
        kwgs = {'error': '用户输入密码错误'}
        return HttpResponseRedirect('/?error=用户输入密码错误')


def registerWork(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    id = generate(size=5)
    cookie = generate(size=10)
    operateInsertUserTable(id, username, password, cookie)
    response = HttpResponseRedirect('/xiaotieba/')
    response.set_cookie(
        'cookie', cookie, expires=datetime.now()+timedelta(days=14))
    response.set_cookie('username', username,
                        expires=datetime.now()+timedelta(days=14))
    # return HttpResponseRedirect(f'/xiaotieba/?username={username}&password={password}')
    return response


def append(request):
    id = generate(size=5)
    appendwords = request.POST.get('appendwords')
    username = request.COOKIES['username']
    now = datetime.now()
    nowTime = now.strftime("%Y-%m-%d %H:%M")
    print(now, nowTime)
    operateInsertContentTable(id, username, appendwords, nowTime)
    return redirect('index')


def search(request):
    return render(request, "xiaotieba/search.html")

def searchWork(request):
    keywords = request.GET.get("keywords")
    return redirect(f'/xiaotieba/search/?keywords={keywords}')

def postSearch(request):
    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    keywords = request.GET.get("keywords")
    # Generate list of posts
    data = getSpecificRowFromContentTable(start, end+1, keywords)
    for i in data:
        print(i)

    # Artificially delay speed of response
    time.sleep(0.5)
    # Return list of posts
    return JsonResponse({
        "posts": data
    })
