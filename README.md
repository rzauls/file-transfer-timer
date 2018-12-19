# file-transfer-timer

A simple python socket-based networks speed measuring tool. Created mainly for RAE555 Riga Technical University coursework.

## Usage

1. Create a desired file size

    * Windows
    ```fsutil file createNew data.dat <size>```
    * Unix
    ```dd if=/dev/zero of=data.dat  bs=<size>  count=1```

2. Run server***.py in directory where data.dat is located (exact name of data file is important) on the first machine
3. Determine IP of the server machine and edit the client script destination IP and the server script host IP
4. Run client***.py on other machine (make sure you have enough free space for the data.dat file on second machine)

(Both server and client have to run on the same protocol (UDP or TCP) else the connection will not work)
