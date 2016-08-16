
# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("10.64.9.142",9000))
s.listen(10)
print u"等待连接"
while 1:
    conn,addr = s.accept()
    print "come :", addr
    while True:
        data = conn.recv(1024)
        if data=="close":
            conn.close()
            break
        print data
        comment = raw_input(u"回复")
        if comment!="close":
            conn.sendall(comment)
            print u"发送成功"
        else:
            conn.close()
