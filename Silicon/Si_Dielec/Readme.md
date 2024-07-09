1. Run scf calc..
2. Run nscf calc..
3. Run eps.in file
```
eps.x <dielec_eps.x> dielec_eps.out
```
This will generate 4 file epsr_silicon.dat epsi_silicon.dat, eels_silicon.dat,ieps_silicon.dat.  
Where epsi is imaginary part of murnghan eq of state which is dielectric constant.  
By using real and imaginary part we can calculate absorption coefficient and plot  
see plot.py
   
