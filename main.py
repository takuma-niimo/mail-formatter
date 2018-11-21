#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
import sys
import io
import re
sys.sdtout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Subfunction
# -----------
def isNextLevel(array, regex):
    for x in array:
        if not regex.search(x):
            return False
    return True

# Detail error report
cgitb.enable()
cgitb.enable(display=0, logdir="./logs")

# Constant value
R = 20

print("Content-Type: text/html; charset=UTF-8\n")
print('<!doctype html>\n<html>\n<head>\n<link rel="stylesheet" href="css/output.css">\n</head>\n<body>\n')
form = cgi.FieldStorage()
if 'mailtext' not in form:
    print('<h1>Error</h1>')
    print('<p>Please fill in the textarea field.</p>')
    exit()

# output = re.sub('\r\n|\r|\n', '<br>', form['mailtext'].value);
orig = re.split('\r\n|\r|\n', form['mailtext'].value)
# print('<p>mailtext:<br>')

# Initialize
patternUpperLevel = r'^> '
level = 1
quoteFlag = False
output = '<details><summary>Mail' + str(level) + '</summary>'

rePattern = re.compile(patternUpperLevel)

for i, line in enumerate(orig):
    line += '<br>\n'

    if rePattern.search(line):
        if quoteFlag:
            output += line.lstrip('> ')

        else:
            if isNextLevel(orig[i:i+R], rePattern):
                level += 1
                output += '</details><details><summary>Mail' + str(level) + '</summary>'
                output += line.lstrip('> ')
                patternUpperLevel += '> '
                rePattern = re.compile(patternUpperLevel)

            else:
                quoteFlag = True
                output += '<blockquote><p>' + line.lstrip('> ')

    else:
        if quoteFlag:
            output += '</p></blockquote>'
            quoteFlag = False
        else:
            output += line.lstrip('> ')

print(output)
print('</body></html>')
