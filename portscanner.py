import socket
import threading
import queue

q=queue.Queue()
for i in range(1,65536):
    q.put(i)
IP=input("Enter the ip address that you want to scan : ")

def scan():
        while not q.empty():
            port=q.get()
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                try:
                    s.connect((IP,port))
                    print(f'Port {port} is open!')
                except:
                   pass
            q.task_done()

for i in range(30):
    t=threading.Thread(target=scan,daemon=True)
    t.start()

q.join()
print("Finished!")
