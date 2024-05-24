import socket

# List of default ports
ports = [21, 22, 80, 443, 445, 3306, 25]

# Iterate through each port in the list
for port in ports:
    # Try to connect and check if the connection is successful ----------

    # Create a socket object for IPv4 and TCP connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout for the connection attempt
    client.settimeout(0.5)
    code = client.connect_ex(("localhost", port))
    if code == 0:
        print(port, "Open")
    else:
        print(port, "Closed")