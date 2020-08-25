#!/usr/bin/python

import nfc
import binascii

def decode(device):
    return binascii.b2a_hex(device).decode("utf-8")

def on_startup(targets):
    return targets

def on_connect(tag):
    print("New contactless device detected, ID #",decode(tag.identifier))

rdwr_options = {
    'targets': ['106A'],
    'on-startup': on_startup,
    'on-connect': on_connect,
}
with nfc.ContactlessFrontend('tty:USB0:pn532') as clf:
    tag = clf.connect(rdwr=rdwr_options)
    print(decode(tag.identifier))
    if tag.ndef:
        print(tag.ndef.message.pretty())