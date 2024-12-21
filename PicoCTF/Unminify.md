# PICO CTF WEB EXPLOITATION!

----

## Unminify

When we launch the instance we get greeted with the following page:

![image_1](p_img/pico_1.png)

And upon using the inspect tool we get this:

![image_2](p_img/Term1.png)

----

## Breakdown

So clearly we get nothing from this just looking at the web inspector alone, will need to find tools that I can use to get this to work.

I decided to use Curl and got the following result:

![image_3](p_img/cmd1.png)

Flag - picoCTF{pr3tty_c0d3_622b2c88}

Curl: Command line tool to transfer data using URL syntax.

What it supports: (Variety of things but mainly used for)
1. HTTP
2. HTTPS
3. FTP
