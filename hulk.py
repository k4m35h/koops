data = '''
[lang:php]
    [config]
        [terminate];[/terminate]
        [template]<?php\n{code}[/template]
    [config]
    [assignment]
        [default]${variable} = {value}[/default]
        [ifelse]${variable} = ({condition})? {value} : {else}[/ifelse]
    [/assignment]
[/lang]
'''
