#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

import os
import argparse

parser = argparse.ArgumentParser(description='Libera a porta na VM para o Docker')
parser.add_argument('ports', nargs='*', help='Porta aberta pelo processo')
parser.add_argument('--remove', '-r', action='store_true', help='Remover a porta')
args = parser.parse_args()

ports = args.ports

os.system('docker-machine stop')
for port in ports:
    os.system('VBoxManage modifyvm "default" --natpf1 ",tcp,127.0.0.1,%s,,%s"' % (port, port))
os.system('docker-machine start')