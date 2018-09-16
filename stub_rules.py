"""
rules = {
    3: 'fizz',
    5: 'buzz',
}

for x in range(1, 100):
    s = ''
    for key, val in rules.items():
        if x % key == 0:
            s += val
    if not s:
        s = str(x)
    print(s)
"""

proto = 'MC'

stub_rules = {
    'MC': [
        {
            'request': [
                {
                    'field': 'DE64.10',
                    'value': ['10', '11', '12'],
                },
                {
                    'field': 'DE61.1',
                    'value': ['20', '21'],
                    'exclude': True,
                }
            ],
            'response': [
                {
                    'field': 'DE62',
                    'value': '10',
                },
                {
                    'field': 'DE33',
                    'value': '30',
                },
            ]
        },
        {
            'request': [
                {
                    'field': 'DE64.10',
                    'value': ['11'],
                },
                {
                    'field': 'DE61.4',
                    'value': ['5'],
                    'exclude': True,
                }
            ],
            'response': [
                {
                    'field': 'DE62',
                    'value': '10',
                },
                {
                    'field': 'DE33',
                    'value': '30',
                },
            ]
        }
    ]
}

messages = {
    'MC': [
        {
            'DE64.10': '10',
            'DE61.1': '22',
            'DE61.5': '15',
        },
        {
            'DE64.10': '11',
            'DE61.1': '5',
            'DE61.5': '2',
        },
        {
            'DE64.10': '10',
            'DE61.1': '10',
        },
        {
            'DE64.10': '15',
            'DE61.1': '10',
            'DE55': '17',
        },
    ]
}


def check_rule(msg, rule):
    field = rule['field']
    value = rule['value']
    exclude = rule.get('exclude')
    if field in msg:
        if exclude:
            if msg[field] in value:
                return False
        else:
            if msg[field] not in value:
                return False
    return True


def apply_rules(msg, rules):
    for rule in rules:
        print(rule['request'])
        if all(check_rule(msg, rec) for rec in rule['request']):
            print('response: {}'.format(rule['response']))


for msg in messages[proto]:
    print(msg)
    rules = stub_rules[proto]
    apply_rules(msg, rules)
