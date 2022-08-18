import pexpect
import sys
from pexpect import popen_spawn
ch= popen_spawn.PopenSpawn('ssh students@172.27.26.188')
ch.expect("students@172.27.26.188's password:")
ch.sendline('cs641a')