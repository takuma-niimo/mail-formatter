#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import cgi
# import cgitb
import sys
import io
import re
from browser import document, alert
# sys.sdtout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Subfunction
# -----------
def isNextLevel(array, regex):
    for x in array:
        if not regex.search(x):
            return False
    return True

def echo(a):
    alert(a)

# # Detail error report
# # cgitb.enable()
# # cgitb.enable(display=0, logdir="./logs")

def output_html(ev):
    alert(document['mail-text'].value)
    exit()
#     # Constant value
#     R = 20

#     echo("Content-Type: text/html; charset=UTF-8\n")
#     exit()
#     echo('<!doctype html>\n<html>\n<head>\n<link rel="stylesheet" href="css/output.css">\n</head>\n<body>\n')
#     # form = cgi.FieldStorage()
#     form = document['mail-text'].value
#     if 'mailtext' not in form:
#         echo('<h1>Error</h1>')
#         echo('<p>Please fill in the textarea field.</p>')
#         exit()

#     # output = re.sub('\r\n|\r|\n', '<br>', form['mailtext'].value);
#     orig = re.split('\r\n|\r|\n', form['mailtext'].value)
#     # echo('<p>mailtext:<br>')

#     # Initialize
#     patternUpperLevel = r'^> '
#     level = 1
#     quoteFlag = False
#     output = '<details><summary>Mail' + str(level) + '</summary>'

#     rePattern = re.compile(patternUpperLevel)

#     for i, line in enumerate(orig):
#         line += '<br>\n'

#         if rePattern.search(line):
#             if quoteFlag:
#                 output += line.lstrip('> ')

#             else:
#                 if isNextLevel(orig[i:i+R], rePattern):
#                     level += 1
#                     output += '</details><details><summary>Mail' + str(level) + '</summary>'
#                     output += line.lstrip('> ')
#                     patternUpperLevel += '> '
#                     rePattern = re.compile(patternUpperLevel)

#                 else:
#                     quoteFlag = True
#                     output += '<blockquote><p>' + line.lstrip('> ')

#         else:
#             if quoteFlag:
#                 output += '</p></blockquote>'
#                 quoteFlag = False
#             else:
#                 output += line.lstrip('> ')

#     echo(output)
#     echo('</body></html>')

document['format'].bind('click', output_html)
