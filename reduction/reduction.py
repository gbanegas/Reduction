
from sage.rings.polynomial.polynomial_gf2x import Polynomial_GF2X
class Reduction:
	def reduction(self, Polynomial_GF2X p):
		if not Polynomial_GF2X.is_irreducible():
			raise Exception("Oops NOT an Irreducible polynomial")

		print "passei"




