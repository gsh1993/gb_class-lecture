"""
Module for square root of a number
"""

def sqrt2(x):
	s=1.0
	kmax=100
	tol=1.0e-14
	for k in range(kmax):
	    s0=s
	    print "before iteration %s, s = %20.15f" %(k,s)
	    s=0.5*(s+x/s)
	    delta_s=s-s0
	    if abs(delta_s/x)<tol:
		break
	print "after %s iterations, s=%20.15f" %(k+1,s)
