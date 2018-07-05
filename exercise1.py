from paramiko import client


class ssh(object):
    client = None

    def __init__(self, address, username, password):
        print("Connecting to the server")

        # transport = self.client.get_transport()
        # transport.auth_none('root')

        # creating a new ssh client
        self.client = client.SSHClient()

        # following line required if you want to access a server that is not yet in the known_hosts file
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())

        # making the connection
        self.client.connect(address, username=username, password=password, look_for_keys=False)
        self.client.invoke_shell()

    def sendCommand(self, command):

        # check if connection is made previously
        if (self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            print(stdin, stdout, stderr)
            while not stdout.channel.exit_status_ready():
                # print stdout data when available
                if stdout.channel.recv_ready():
                    # retrieve first 1024 bytes
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata

                    print(alldata)

        else:
            print("Connection not opened")


connection = ssh("10.134.148.198", "tcs", "tcs@1234")
connection.sendCommand("ls /etc/")



