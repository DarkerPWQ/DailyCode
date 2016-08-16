# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.64.9.142",9000))
print u"连接上"
while True:
    comment = raw_input(u"回复")
    if comment!="close":
        s.sendall(comment)
        print u"发送成功"
    else:
        s.sendall(comment)
        s.close()
        break
    data = s.recv(1024)
    print data
