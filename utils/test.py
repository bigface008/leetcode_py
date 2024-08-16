def tst(desc, output, expect):
    if output == expect:
        print(f'[PASSED] {desc} output={output} expected={expect}')
    else:
        print(f'[FAILED] {desc} output={output} expected={expect}')