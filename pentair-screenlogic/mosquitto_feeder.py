import paho.mqtt.client as mqtt
import time
import sys
import re


def main(argv):
  client = mqtt.Client()
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
