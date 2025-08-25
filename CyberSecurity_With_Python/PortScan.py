from scapy.all import * 
import ipaddress

ports = [25, 80, 53, 443, 445, 8080, 8443]

# Function that sends SYN packets to inputted host and waits for reply
def SynScan(host):
    ans,unans = sr(
        IP(dst-host)
        TCP(sport=33333,dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open ports at %s:" %host)
    for (s,r) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP]flags=="SA":
            print(s[TCP].dport)

# Function to test if there is a DNS service running on the machine using the given address
def DNSScan(host):
    ans,unans = sr(
        IP(dst-host)/
        UDP(dport=53)/
        DNS(rd=1,qd=DNSQR(qname="google.com)"), timeout=2,verbose=0)
    )
    if ans and ans[UDP]:
        print("DNS Server at %s" %host)

# Actual script to prompt user to enter an ip address 

host = input("enter IP address: ")
try:
    ipaddress.ip_address(host)
except:
    print("Invalid address")
    exit(-1)

SynScan(host)
DNSScan(host)