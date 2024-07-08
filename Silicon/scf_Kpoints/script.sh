NAME="kpoints"

for KPOINT in 4 6 8 10 12 14
do
cat > ${NAME}_${KPOINT}.in << EOF
&control
    calculation = 'scf'
    restart_mode='from_scratch',
    prefix='silicon',
    tstress = .true.
    tprnfor = .true.
    pseudo_dir = './',
    outdir='./'
 /
 &system
    ibrav=  2, celldm(1) =10.20, nat=  2, ntyp= 1,
    ecutwfc = 35.0,
 /
 &electrons
    mixing_mode = 'plain'
    mixing_beta = 0.7
    conv_thr =  1.0d-8
 /
ATOMIC_SPECIES
 Si  28.086  Si.pbesol-n-rrkjus_psl.1.0.0.UPF
ATOMIC_POSITIONS alat
 Si 0.00 0.00 0.00
 Si 0.25 0.25 0.25
K_POINTS {automatic}
$KPOINT $KPOINT $KPOINT 0 0 0
EOF

pw.x < ${NAME}_${KPOINT}.in > ${NAME}_${KPOINT}.out
echo ${NAME}_${KPOINT}
grep ! ${NAME}_${KPOINT// /_}.out

done
