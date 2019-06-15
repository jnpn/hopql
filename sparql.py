from pprint import pprint
from grako import parse

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

select = 'SELECT' vars
  ;

vars = @+:var {',' @+:var}*
  ;

where =
  | 'WHERE' '{' [clauses] '}'
  | 'WHERE' '{' [clauses options] '}'
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

option = 'OPTIONAL' '(' clause ')' ;

orderby = 'ORDER BY' vars ;

limit = 'LIMIT' int ;

offset = 'OFFSET' int ;
'''

SAMPLE = 'sparql.dsl'
def test():
    with open(SAMPLE) as dsl:
        src = dsl.read()
        print('input DSL:')
        print(src)
        ast = parse(SPARQL, src, eol_comments_re="#.*?$")
        print('output AST:')
        pprint(ast)
