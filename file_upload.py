#!/usr/bin/python

import cgi, os, time
import cgitb; cgitb.enable()
from PlayerEditor import *
from PatchFileGenerator import *
from Values import *


form = cgi.FieldStorage()
message = ""

# Get filenames here from POST
file_item1 = form['rbi3_1990_file']
file_item2 = form['csv_file']
file_item3 = form['new_file_name']
# new modified game filename with full directory
new_file_name = ROOT_DIRECTORY + 'upload\\' + str(file_item3.value)
# just the filename so it can be inserted into a download URL
filename_for_url = str(file_item3.value)


# Test if the original game file was uploaded
if file_item1.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    rbi3_1990_file = ROOT_DIRECTORY + 'upload\\' + os.path.basename(file_item1.filename)
    # NOTE: on brahm.ca read/write permissions have to be set for folders via admin.brahm.ca control panel
    open(rbi3_1990_file, 'wb').write(file_item1.file.read())
else:
    message += 'No RBI 3 1990 file was uploaded or there was an error.'


# Test if the csv file was uploaded
if file_item2.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    csv_file = ROOT_DIRECTORY + 'upload\\' + os.path.basename(file_item2.filename)
    # NOTE: on brahm.ca read/write permissions have to be set for folders via admin.brahm.ca control panel
    open(csv_file, 'wb').write(file_item2.file.read())
else:
    message += 'No csv file was uploaded or there was an error.'


#test if a valid filename was given - if not, add to error message.
if filename_for_url == "" or filename_for_url[4:].lower() != ".nes":
    message += "<br>There was a problem with the filename you provided - it must end in .nes<br>"
else:
    # patch the uploaded 1990 file with the latest patchfile
    modify_1990_file(rbi3_1990_file, ROOT_DIRECTORY + 'data_files/2013patchfile.pch',
                     new_file_name)
    # create a player editor instance so the .csv file can be applied to it
    editor = PlayerEditor(new_file_name)
    # import the .csv data and write it into the player editor instance
    editor.import_new_data(csv_file)
    # wrap it up and create the new game file.
    editor.write_game_file(new_file_name)


# delete the uploaded files (whether creating the new ROM file was successful or not)
os.remove(rbi3_1990_file)
os.remove(csv_file)


# if message is blank so far, the ROM creation was successful, so let's give some good news and serve a download URL
if message == "":
    message += '<br><br>All done! Your new patched game file can be downloaded here (right-click, Save As):<br>'
    message += '<a href="http://brahm.ca/rbi/dev/bntest/upload/' + filename_for_url +\
               '" type="application/octet-stream">DOWNLOAD</a><br>'
    message += '<b>This file will be deleted from the server in 5 minutes</b>.'

# to do: make the output page prettier
print """\
Content-Type: text/html\n
<html><body>
   <p>%s</p>
</body></html>
""" % (message,)

# sleep for a period of time (5 minutes) and delete the newly created file
# is there a better way to do this?
time.sleep(300)
os.remove(new_file_name)