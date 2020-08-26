import nfc
import threading
import binascii

def decode(device):
    return binascii.b2a_hex(device).decode("utf-8")

def on_startup(targets):
    print("Esperando un dispositivo (nfc)...")
    return targets

def on_connect(tag):
    print("New contactless device detected, ID #",decode(tag.identifier))

def scan():
    with nfc.ContactlessFrontend('tty:USB0:pn532') as clf:
        tag = clf.connect(rdwr={'targets': ['106A'],'on-startup': on_startup,'on-connect': on_connect})
        if tag.ndef:
            print(tag.ndef.message.pretty())
        return (decode(tag.identifier))