from collections import namedtuple
from pprint import pprint
from grako import parse

######################################################################## GRAMMAR

SPARQL = '''
@@grammar::Sparql

start = query $ ;

query
   = select:select
     [where:where]
     [orderby:orderby]
     [limit:limit]
     [offset:offset]
   ;

select = 'SELECT' @:vars
  ;

vars = @+:var {',' @+:var}*
  ;

where =
  | 'WHERE' '{' [clauses:clauses] '}'
  | 'WHERE' '{' [clauses:clauses options:options] '}'
  ;

clauses = @+:clause {'.' @+:clause}*
  ;

clause = object predicate object
  ;

object = var | constant ;

var = '?' @:/\w+/;

constant = str | int ; # | float ;

str = /"[^"]*"/ ;
int = /\d+/ ;
#+TODO: Fix float parsing in clause.
# float = int [frac] [exp] ;
# frac = '.' int ;
# exp = e int ;
# e = ('e'|'E') ('+'|'-') ;

predicate = /\w+/ ;

options = {option}+ ;

option = 'OPTIONAL' '(' @:clause ')' ;

orderby = 'ORDER BY' @:vars ;

limit = 'LIMIT' @:int ;

offset = 'OFFSET' @:int ;
'''


######################################################################## CLASSES

# Select, Where, Offset, Limit, Clause, Var, Int, Float, Str
Select = namedtuple('Select', 'vars')
Where = namedtuple('Where', 'clauses options')
Offset = namedtuple('Offset', 'offset')
Limit = namedtuple('Limit', 'limit')
Clause = namedtuple('Clause', 'left pred right')
Predicate = namedtuple('Predicate', 'pred')
Var = namedtuple('Var', 'var')
Int = namedtuple('Int', 'int')
Float = namedtuple('Float', 'float')
Str = namedtuple('Str', 'str')

class SparqlSemantics:
    def predicate(self, n):
        return Predicate(n)
    def str(self, s):
        return Str(s[1:-1])
    def var(self, v):
        return Var(v)
    def int(self, i):
        return Int(int(i))

######################################################################## MAIN

SAMPLE = 'sparql.dsl'
def test():
    with open(SAMPLE) as dsl:
        src = dsl.read()
        print('input DSL:')
        print(src)
        sem = SparqlSemantics()
        ast = parse(SPARQL, src, eol_comments_re="#.*?$", semantics=sem)
        print('output AST:')
        pprint(ast)
        return ast
