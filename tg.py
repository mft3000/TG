#! /usr/bin/env python2.7

import sys

try:
    from scapy.all import *
except:
    print "install scapy"


def usage():
  print "Usage: tg.py 8.8.8.8 SIZE TOS MBPS SEC"
  sys.exit(1)
	
if len(sys.argv) != 6:
	usage()
else:
	s=int(sys.argv[2])
	s1=s
	t=int(sys.argv[3])
	mb=int(sys.argv[4])
	time=int(sys.argv[5])
	if int(s)<=1500:
		s=int(sys.argv[2])
		s=1500-42
	else:
		print "Packet too big"
		sys.exit(1)


a=IP(dst=sys.argv[1],tos=t)/ICMP()/Raw(RandBin(size=s))
#a=IP(dst=sys.argv[1],tos=t)/TCP(sport=1024,dport=666)/Raw(RandBin(size=s))
#a=IP(src="93.189.184.1",dst=sys.argv[1],tos=t)/UDP(sport=1024,dport=666)/Raw(RandBin(size=s))
b=Ether()/a
print '-----'
print len(b)
print '-----'
print b.show()
print '-----'
pps=mb*(2**20)/8/s1
nl=pps*time
#sendpfast(b,iface='en0',mbps=mb,loop=nl,file_cache=True)
sendpfast(b,iface='en0',pps=pps,loop=nl,file_cache=True)
