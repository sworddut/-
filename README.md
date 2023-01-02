#  Build a server

你可以使用一下代码运行服务器，必须保证该目录下有manage.py文件

```shell
D:\webProject\小贴吧\minitieba>  python manage.py runserver 0.0.0.0:8000  
```

# Open a client

打开你的浏览器输入一下任意网址:

```python
http://localhost:8000/
http://127.0.0.1:8000/
http://{your private ip address}:8000/
```

如果你使用最后一个网址，你可以在关闭防火墙的前提下，用你的手机内网访问该网站。内网ip可以通过```ipconfig```查询。

