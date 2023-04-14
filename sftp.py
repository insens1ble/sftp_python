#!/usr/bin/python3.9

import paramiko
# paramiko.util.log_to_file("paramiko.log")

# Open a transport
host,port = "IP",PORT
transport = paramiko.Transport((host,port))

# Auth
username,password = "username","password"
transport.connect(None, username, password)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)

# Download
filepath = "path"
localpath = "localpath"

# filesInSFTP = sftp.listdir_attr('/home/sftpuser/numlex/Numbering_Plan/')
# filesInSFTP.sort(key = lambda f: f.st_mtime)

latest = 0
latestfile = None

fileAttrs = sftp.listdir_attr(filepath)

for fileattr in fileAttrs:
    if fileattr.st_mtime > latest:
        latest = fileattr.st_mtime
        latestfile = fileattr.filename
print(latestfile)
if latestfile is not None:
    sftp.get(filepath + latestfile, localpath + latestfile)

# Close
if sftp: sftp.close()
if transport: transport.close()
