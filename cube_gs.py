x=10000.
s=1.
kmax=100
tol=1.0e-14
for k in range(kmax):
	s0=s
	s=2*s/3+x/3/s/s
	delta_s=s-s0
	if abs(delta_s)<tol:
		break
	print "after %s iterations, s=%20.15f" %(k+1,s)
