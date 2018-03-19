import re
data = '''
[config]
    [lang]php[/lang]
    [terminate];[/terminate]
    [template]<?php\n{code}[/template]
    [block]{\n{code}\n}[/block]
[/config]
[assignment]
    [default]${variable} = {value}[/default]
    [ifelse]${variable} = ({condition})? {value} : {else}[/ifelse]
[/assignment]
'''

bbcode = re.compile(r'\[([a-z]+)\]([^\0]+)\[/\1\]', re.M|re.I)

def convert(data):
    node = {}
    process = bbcode.findall(data)
    if len(process) == 0:
        return data
    for itm in process:
        node[itm[0]] = convert(itm[1])
    return node

print convert(data)
