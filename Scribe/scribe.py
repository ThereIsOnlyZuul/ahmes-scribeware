from Templates.additionTemplate import AdditionTemplate
from Templates.babylonianSquareRootsTemplate import BabylonianSquareRootsTemplate
from Templates.egyptianFractionsTemplate import EgyptianFractionsTemplate
from Generics.template import ProblemPart


class Scribe:

	templates = {'addition1': AdditionTemplate(),
		'babylonian1': BabylonianSquareRootsTemplate(),
		'egyptian1': EgyptianFractionsTemplate()}

	def __init__(self, corpus=None):
		self.corpus = corpus

	def write(self,template,out):
		self.corpus = self.templates[template]
		self.corpus.out(out)
		self.corpus.build()
		self.corpus.create()