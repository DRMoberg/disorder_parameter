#!/bin/bash

if [ $# -ne 2 ]; then
   echo "usage: ./do_Disorder.sh init_run fin_run"
else

   # set number of runs to combine
   s=$1
   t=$2

   nst='ls st.* | wc -l'

   if [ $nst -gt 0 ]; then
      rm -f hist* Ocoords.* sortO.* st.* HISTORY_PIMD_full
   fi

   # combine runs into 1 file
   for ((i=$s; i<=$t; i++)); do
      rm -f history_pimd.$i
      ln -s run$i/HISTORY_PIMD.01 history_pimd.$i
      cat history_pimd.$i >> HISTORY_PIMD_full
   done

   # split full HISTORY file into n separate history.# files
   python HISTORY_splice.py HISTORY_PIMD_full

   # calculate the number of frames
   n="$(ls -d history.* | wc -l)"
   echo "loaded $n frames"

   # loop over n history.# files
   rm st_all.txt st_ave.txt st_ave_sort.txt
   for ((i=0; i<$n; i++)); do
      python HISTORYtoOcoords.py history.$i

      # sort coordinates by z values in ascending order
      sort -g -k 3 Ocoords.$i > sortO.$i

      # calculate S_T for each frame in run
      python DisorderParam.py sortO.$i st.$i

      # concatenates S_T files, then averages and sorts by layer #
      cat st.$i >> st_all.txt
      awk '{sum[$1]=sum[$1] + $2; nr[$1]++} END {for (a in sum) {print a, sum[a]/nr[a]}}' st_all.txt > st_ave.txt
      sort -n -k 1 st_ave.txt > st_ave_sort.txt

      rm st.$i sortO.$i Ocoords.$i history.$i

      if [ $(($i % 25)) == 0 ]; then
         echo "st.$i done..."
      fi
   done

fi
