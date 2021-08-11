#!/bin/bash
sudo gatttool -b 00:22:D0:75:A7:4F --char-write-req --handle=0x0013 --value=0100 --listen | python polar_h7.py