import socket
import time
from threading import Thread
from multiprocessing import Lock, Queue, Event
import sys
UDP_IP = "localhost"
OUTBOUND_PORT = 7500
INBOUND_PORT = 7501
SEND_DESTINATION = (UDP_IP, OUTBOUND_PORT)

def socket_thread(in_socket, out_socket, out_lock, recieve_queue, stop_func):
    in_socket.setblocking(False);
    while not stop_func():
        try:
            data, addr = in_socket.recvfrom(1024)
            decoded_data = data.decode("utf-8")
            hitting_player,hit_player = decoded_data.split(":")
            recieve_queue.put((int(hitting_player),int(hit_player)))
            with out_lock:
                out_socket.sendto(hit_player.encode("utf-8"),SEND_DESTINATION)
        except:
           pass
      

class udpHandler:
    def __init__(self):
       self.outbound_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
       self.inbound_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
       self.inbound_socket.setblocking(True);
       self.inbound_socket.bind(("",INBOUND_PORT))
       self.queue = Queue()
       self.stop_thread = False; 
       self.outbound_lock = Lock()
       self.listeningthread = Thread(target=socket_thread,args=(self.inbound_socket,self.outbound_socket,self.outbound_lock,self.queue, self.stop_func)) 
       self.listeningthread.start()
       #time.sleep(0.01)
       
    def stop_func(self):
        return self.stop_thread
  
    #takes in the equipment_id and transmits it
    def transmit_equipment_id(self, equip_id):
        with self.outbound_lock:
            self.outbound_socket.sendto(str(equip_id).encode("utf-8"),SEND_DESTINATION)

    #transmits the starting code
    def transmit_start(self):
        with self.outbound_lock:
            self.outbound_socket.sendto("202".encode("utf-8"),SEND_DESTINATION)

    def transmit_end(self):
        with self.outbound_lock:
            for _ in range(3):
                self.outbound_socket.sendto("221".encode("utf-8"),SEND_DESTINATION)


   #returns a list containg all new alerts since the last time this method was called
    def pop_alerts(self):
        alerts = []
        while not self.queue.empty():
            alerts.append(self.queue.get())
        return alerts;

    def shutdown(self):
        self.stop_thread = True



handler_instance = udpHandler()

def get_instance():
    return handler_instance
    

if __name__ == "__main__":
    handler = get_instance()
    handler.transmit_equipment_id(1)
    handler.transmit_equipment_id(2)
    handler.transmit_equipment_id(3)
    handler.transmit_equipment_id(4)
    handler.transmit_start()
    for _ in range(10):
        for alert in handler.pop_alerts():
            print(alert)
        time.sleep(3);
    handler.transmit_end()
    handler.shutdown()
    sys.exit(0)

