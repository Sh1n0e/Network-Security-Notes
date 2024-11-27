# HackTheBox Journey

What have I learnt so far:
1. Using OpenVPN Files to be able to connect to the same network as whatever machine I am trying to find the flag from.
2. Using tools like nmap to be able to find exposed ports on any given network

Expanding upon point 2, HackTheBox so far has taught me how to exploit services like:
- Telnet
- SSH: Secure Shell
- FTP: File Transfer Protocol
- SMB: Server Message Block
- Redis: Remote Dictionary Server

I will follow-up with my understanding on each service below:

----

# Redis - Remote Disctionary Server

![RedisImage](h_img/Rdis.png)

Redis is an open-source, in memory, multimodel database that works super fast.

- Is a system where Read and Write Operations happen quickly on RAM rather than the disk (which would be slower)
- Still utilizes the disk for storage to be reconstructed whenever needed.

Data within this database is stored in 2 parts: Key and Value (Value is self explanatory)

## Key 
Can be stored as a string, bitmap, bitfield, hash, list, set, sorted set etc. etc.

These are stored in a similar way any programming language would store a variable rather than having to make one or many tables to store any given data set.

## Basic Commands 

``` c#
SET <Key> <String> - Creates a Key with a STRING Value

GET <Key> - Reads data within a Key
```

Redis itself is able to act as a primary database.

----

# How did I use this in practice?

1. Regular reconnaisance by utilizing nmap to scan for open ports (by default, runs on port 6379)
2. With the nmap scan it actually shows that the service is indeed running on that same port

(Would show a screenshot but I didn't think about making this when I was doig this lab)

By using the following command I am able to get access to the Database via the command line:

``` c#
redis-cli -h <x.x.x.x>

x.x.x.x:6379> 
```

From here I can use the keys*  to find where the flag would be located:

``` c#
x.x.x.x:6379> keys *
1) "temp"
2) "stor"
3) "numb"
4) "flag"
```

Then I am able to use the GET command on the 4th key (flag) to get what I need to complete this task!