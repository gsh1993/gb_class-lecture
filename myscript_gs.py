x=10000.0
s=1.0
kmax=100
tol=1.0e-14
for k in range(kmax):
    s0=s
    print "before iteration %s, s = %s" %(k,s)
    s=0.5*(s+x/s)
    delta_s=s-s0
    if abs(delta_s/x)<tol:
	break

print "after %s iterations, s=%s" %(k+1,s)
