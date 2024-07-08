To run input file use the following command->
pw.x < si.scf.in > si.scf.out

For parallel excecution->
mpirun -np 4 pw.x < si.scf.in > si.scf.out

To run in background->
mpirun -np 4 pw.x < si.scf.in > si.scf.out &
tail -f si.scf.out ## see live output

To run script file->
./si_script.sh
or 
sh si_script.sh

To plot .dat file
xmgrace Si.dat
or write a .py file and run it by python.py
