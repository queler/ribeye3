#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    # NOTE: on brahm.ca read/write permissions have to be set for folders via admin.brahm.ca control panel
    open(r'D:\Inetpub\vhosts\brahm.ca\httpdocs\rbi\dev\bntest\upload\'' + fn, 'wb').write(fileitem.file.read())

    message = 'The file "' + fn + '" was uploaded successfully'
   
else:
    message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,)