import paho.mqtt.client as mqtt
import platform
import time
import sys
import re
import os


def main(argv):
  my_host = platform.node()
  my_pid = os.getpid()
  client_id = my_host + '-' + str(my_pid)

  client = mqtt.Client(client_id)
  client.username_pw_set(username=argv[3], password=argv[4])
  client.connect(argv[1], int(argv[2]) , 60)
  client.loop_start()

  for line in sys.stdin:
    m = re.match('(.*),(.*)', line)
    if m:
      client.publish(m.group(1), payload=m.group(2))

  time.sleep(2)
  client.loop_stop()

if __name__ == "__main__":
    main(sys.argv)
