import paramiko
from io import StringIO

def sshcommand(host,username,port,privatekey,command,printlinies=True):

    ssh_privatekey = f"""\
-----BEGIN OPENSSH PRIVATE KEY-----
{privatekey}
-----END OPENSSH PRIVATE KEY-----"""

    pkey = paramiko.RSAKey.from_private_key(StringIO(ssh_privatekey))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, pkey=pkey)
    stdin, stdout, stderr = ssh.exec_command(command)
    lines= stdout.readlines()
    if printlinies==True:
        print(lines)
    ssh.close()
    return lines