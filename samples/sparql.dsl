# this is a prelude
SELECT ?a, ?b
WHERE {
  ?s IS "foo" .
  ?i IS 42 .
  ?f IS 20.3e7
  OPTIONAL(?u HAS ?v)
}
ORDER BY ?a, ?z
LIMIT 10 OFFSET 0
# and the epilog
