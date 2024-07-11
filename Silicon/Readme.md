Command to visualize the structure.
```
xcrysden --pwi si.scf.in
vesta POSCAR
```

By running cutoff energy and Kpoint calculations (scf) converged value of these can found out.  

Now it is time to find the band struture of Si, which here is started with primitive cell of silicon (2 atoms).  

Just out of curiosity let see if we can get the same band structure and DOS for unitcell (8 atoms) of silicon or 2x2x2 Supercell(16 atoms) of silicon. However after looking at the results it can be seen that DOS is pretty much the same, but the bands structure isn't. So what could be the reaosn?  

Well, the reason is the squeezing of Brillouin zone, which can be obserbed by looking at mirrored bands in band structure.This can be undurstood as the folding of bands (at this point we should go & read about it).  

Also, the binding energy, absorption coefficient, and bulk modulus have been calculated here.

