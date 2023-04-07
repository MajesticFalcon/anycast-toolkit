#!/usr/bin/python3
import subprocess
from sys import stdout
from time import sleep

while True:
  try:
    subprocess.check_output("dig google.com @127.0.0.1", shell=True, timeout=1)
    stdout.write('announce route {IP} next-hop self community [395:555]' + '\n')
    stdout.flush()
  except:
    stdout.write('withdraw route {IP} next-hop self community [395:666]' + '\n')
    stdout.flush()
  sleep(10)
