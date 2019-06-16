import sparql as s

def test_sel1():
    src = 'samples/sel1.dsl'
    assert s.test(src)

def test_sel1whe1flo():
    src = 'samples/sel1whe1flo.dsl'
    assert s.test(src)

def test_sel1whe1int():
    src = 'samples/sel1whe1int.dsl'
    assert s.test(src)

def test_sparql():
    a = s.test('samples/sparql.dsl')
    print(a)
    assert a
