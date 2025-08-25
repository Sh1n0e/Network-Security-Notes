# Writeup for Portscan.py

This is dedicated for writing up my learning and understanding about how the portscan script works.

### What does it do?

This script based on a quick glance over from the book works in a similar way to nmap. Essentially what it does is it takes an IP address and then do a scan to detect any open ports of a user inputted IP address.

This is done using the scapy library which has the following functions:
1. Packet crafting: As the function says, we can basically create "packets" that can be sent forward over the network to test for anything we would need to test for.
2. Packet sniffing and analysis: It can also be used to capture packets and store them to be analyzed for later.
3. Network discovery and scanning: Scan for open ports, activ ehosts and mapping a topology.
4. Automation of network tasks: Can be integrated to automate tedious and complex network tasks.

### How does it work

To keep things brief, the script simply does scans of the following:
1. SYN scan: This scan sends a TCP SYN packet to a port awaiting for a response from the destination address.
2. DNS scan: Tests to see if a DNS server is running on the target address

These functions are implemented in their definitions that can be seen with the following:

```python
# Function that sends SYN packets to inputted host and waits for reply
def SynScan(host):
    ans,unans = sr(
        IP(dst=host)/
        TCP(sport=33333,dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open ports at %s:" %host)
    for (s,r) in ans:
        if r.haslayer(TCP) and r[TCP].flags == 0x12: # Flag for SYN-ACK
            print(s[TCP].dport)

# Function to test if there is a DNS service running on the machine using the given address
def DNSScan(host):
    ans,unans = sr(
        IP(dst=host)/
        UDP(dport=53)/
        DNS(rd=1,qd=DNSQR(qname="google.com"))
        ,timeout=2,verbose=0)
    if ans and ans[UDP]:
        print("DNS Server at %s" %host)
```

And we can actually see in a wireshark capture of the network as I executed the script that SYN packets were sent out via port 443 (HTTPS) and that was how the script is able to return to the client (In this case my raspberry pi) open ports.

Below is the output of me running the command to an IP address that is present in my home network (changed to x's for obvious reasons)

```yaml
pi@cutiepi:~/Network-Security-Notes/CyberSecurity_With_Python $ sudo python3 PortScan.py
enter IP address: x.x.x.x
Open ports at x.x.x.x:
80
53
443
DNS Server at x.x.x.x
```

The book does also have additional exercises I can and will be working on, which can be seen in the comments at the bottom of the file and I will update this writeup as I work on it.

### Extra exercises

