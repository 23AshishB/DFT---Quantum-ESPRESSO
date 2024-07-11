Commands to visulize the structure.
```
xcrysden --pwi Nio.scf.in
vesta POSCAR
```
Use ultra soft pseudo potential.
First perform a usual band structure calculation, but the resultant bands structure or DOS suggests that Nio is metal, which it is not.  

Then add magnetization (AFM), which requires doubling of the cell being used. This gives rise to some potential, and from the band structure and DOS, a small band gap can be seen. However this does not exlain its insulating porperty.  

Now it is time to add U (Hubbard Parameter). After calculating the band structure and DOS, a huge band gap of around 4-5 ev can be seen, which suggests that Nio is an insulator.
