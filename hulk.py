import re
data = '''
[config]
    [terminate];[/terminate]
    [template]<?php\n{code}[/template]
[/config]
[assignment]
    [default]${variable} = {value}[/default]
    [ifelse]${variable} = ({condition})? {value} : {else}[/ifelse]
[/assignment]
'''
print re.findall(r'\[([a-z]+)\]([^\0]+)\[/\1\]',data, re.M|re.I)
