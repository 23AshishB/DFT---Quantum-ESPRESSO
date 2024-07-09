#!/bin/sh
NAME="para"

for PARA in  9.96 10.01 10.06 10.11 10.16 10.21 10.26 10.31 10.36 10.41 10.46 10.51 10.56
do
cat > ${NAME}_${PARA}.in << EOF
 &control
    calculation = 'scf',
    prefix = 'silicon'
    outdir = './tmp/'
    pseudo_dir = './pseudos/'
 /
 &system
    ibrav =  2,
    celldm(1) = $PARA,
    nat =  2,
    ntyp = 1,
    ecutwfc = 50,
 /
 &electrons
    mixing_beta = 0.6
 /

ATOMIC_SPECIES
 Si 28.086  Si.pbesol-n-rrkjus_psl.1.0.0.UPF

ATOMIC_POSITIONS (alat)
 Si 0.0 0.0 0.0
 Si 0.25 0.25 0.25

K_POINTS (automatic)
  8 8 8 0 0 0
EOF

pw.x < ${NAME}_${PARA}.in > ${NAME}_${PARA}.out
echo ${NAME}_${PARA}
grep ! ${NAME}_${PARA}.out

done
