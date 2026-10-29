import numpy as np

def SolveKeppler( m : float, e : float):

	bigE : float
	if e < 0.8:
		bigE = m
	else:
		bigE = np.pi

	for i in range(100):
		f : float = bigE - (e * np.sin(bigE)) - m
		fp : float = 1.0 - (e * np.cos(bigE))
		dE : float = f / fp

		bigE -= dE
		if abs(dE) < 1e-13:
			break

	return bigE

print("E is", SolveKeppler(4.391197906143, 0.1914901069), "correct within 4 sig fig of the real 4.222357813706")