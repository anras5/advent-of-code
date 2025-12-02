#!/bin/bash

counter=0
for line in $(cat "$1");
do
  IFS=$','; split=($line); unset IFS;

  for i in "${!split[@]}"; do

    IFS=$'-'; range=(${split[i]}); unset IFS;
    start=${range[0]}
    end=${range[1]}
    echo "Range: $start to $end"

    for ((j=start; j<=end; j++)); do

        length=${#j}
        firstHalf="${j:0:length/2}"
        secondHalf="${j:length/2}"
        if ((length % 2 == 0)); then
            if [ $firstHalf == $secondHalf ]; then
                counter=$((counter + j))
            fi
        fi

    done

  done

done

echo $counter
