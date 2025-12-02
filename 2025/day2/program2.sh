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

        for ((k=1; k<=length/2; k++)); do
            cut=${j:0:k}
            repeat=$((length / k))
            newValue=$(
                for ((l=1; l<=repeat; l++)); do
                    printf "%s" "$cut"
                done
            )

            if [ $newValue == $j ]; then
                echo "$j: $cut $repeat $newValue"
                counter=$((counter + j))
                break
            fi
        done

    done

  done

done

echo $counter
