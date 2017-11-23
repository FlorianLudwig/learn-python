print('truth-testing')

VALUES = [1, "1", 0, '0', -1, '-1', '',
    [],
    [1],
    [False],
    [0],
    {},
    {1: 'a'}
]

for v in VALUES:
    if v:
        print('yeah', repr(v))
    else:
        print('nope', repr(v))
