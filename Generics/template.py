import os
from enum import Enum

from pylatex import Document, Section, Command, Enumerate
from pylatex.base_classes import Environment
from pylatex.package import Package
from pylatex.utils import NoEscape

from Generics.problem import Problem
from Generics.problemCollection import ProblemCollection

class Template:
	"""
	Template.py - a generic template for a Scribe

	# Attributes:
		collections - a list of the ProblemCollections in the template
		output_file - a string for the location where the output file should reside 
		 (minus any extensions.)
		doc - the LaTeX document


	# Methods:
		create - create a LaTeX file from the collections
	"""

	def __init__(self):
		self.collections = []
		self.output_file = "a"
		self.doc = Document('a')

	# Methods called by the Scribe
	def out(self,output_file_location):
		"""Specify where the output should go"""
		the_file = os.path.join(output_file_location)
		self.output_file = the_file

	def build(self):
		self.autocollect(ProblemPart.QUESTION)
		self.doc.append(NoEscape(r'\newpage \setcounter{section}{0}'))
		self.autocollect(ProblemPart.ANSWER)


	def create(self):
		"""generate a pdf from the sections"""
		self.doc.generate_pdf(self.output_file, clean_tex=False)

	def _setup(self):
		"""load packages etc"""
		self.doc.packages.append(Package('geometry',options='margin=1in'))

	# Behavior methods for Subclasses

	def add_section(self,section_title,section_content):
		"""A generic method for adding sections to a document"""
		with self.doc.create(Section(section_title)):
			self.doc.append(section_content)

	def add_collection(self,collection):
		"""Add collections to the template"""
		self.collections.append(collection)

	def autocollect(self,problem_part):
		"""create sections from the collections"""
		for collection in self.collections:
			with self.doc.create(Section(collection.name)):
				target_env = self.doc
				#only add the instructions before the questions
				if collection.instructions != None and problem_part.value != 'answer':
					self.doc.append(collection.instructions)
				if collection.cols > 1:
					with self.doc.create(Multicols(arguments=str(collection.cols))) as multicol:
						target_env = multicol
				with target_env.create(Enumerate()) as enum:
					for problem in collection.problems:
						# only give the requested problem_part
						if problem_part.value == 'question':
							enum.add_item(problem.question())
						elif problem_part.value == 'answer':
							enum.add_item(problem.answer())


	def add_title(self):
		"""Add the title to the document"""
		self.doc.append(NoEscape(r'\maketitle'))

	def preamble(self,title,author="Homework Zombie",date=NoEscape(r'\today')):
		"""Edit the title information"""
		self.doc.preamble.append(Command('title',title))
		self.doc.preamble.append(Command('author',author))
		self.doc.preamble.append(Command('date', date))

class ProblemPart(Enum):
	QUESTION = "question"
	ANSWER = "answer"

class Multicols(Environment):
	_latex_name = 'multicols'
	packages= [Package('multicol')]
	escape=False
	content_seperator='\n'