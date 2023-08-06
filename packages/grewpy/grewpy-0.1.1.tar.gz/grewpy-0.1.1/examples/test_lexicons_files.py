import sys
import os.path
import json
sys.path.insert(0,os.path.abspath(os.path.join( os.path.dirname(__file__), "../"))) # Use local grew lib

from grewpy import Graph, GRS

graph = Graph("examples/resources/test_lexicon.conll")

print (graph)

string_grs = """
rule set_gender {
  pattern { N [upos=NOUN, !Gender, lemma=lex.noun] }
  commands { N.Gender = lex.Gender }
}
#BEGIN lex
noun\tGender
%-------------
garçon\tMasc
maison\tFem
maison\tMasc
#END
"""
grs = GRS(string_grs)

rewritten_graphs = grs.run(graph, strat = "Iter(set_gender)")

for g in rewritten_graphs:
  print (g.to_conll())

