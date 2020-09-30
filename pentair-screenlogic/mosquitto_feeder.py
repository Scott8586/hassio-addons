import paho.mqtt.client as mqtt
import platform
import time
import sys
import re
import os

def on_connect(client, userdata, flags, return_code):
    """function to mark the connection to a MQTT server
    """

    if return_code != 0:
        print("Connected with result code: ", str(return_code))
    else:
        client.connected_flag=True


def main(argv):
  my_host = platform.node()
  my_pid = os.getpid()
  client_id = my_host + '-' + str(my_pid)

  mqtt.Client.connected_flag=False #create flag in class
  client = mqtt.Client(client_id)
  client.on_connect=on_connect  #bind call back function
  client.username_pw_set(username=argv[3], password=argv[4])
  client.connect(argv[1], int(argv[2]) , 60)
  client.loop_start()
  while not client.connected_flag: #wait in loop
    time.sleep(1)

  for line in sys.stdin:
    line.rstrip()
    m = re.match('(.*),(.*)', line)
    if m:
      msg_info = client.publish(m.group(1), payload=m.group(2))
      if msg_info.is_published() == False:
        msg_info.wait_for_publish()

  time.sleep(2)
  client.loop_stop()
  client.disconnect()

if __name__ == "__main__":
    main(sys.argv)
