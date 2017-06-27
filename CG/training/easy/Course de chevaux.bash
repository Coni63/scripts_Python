read N

for (( i=0; i<N; i++ )); do
    read Pi
    tab[$i]=$Pi
done

tab=($(for each in ${tab[@]}; do echo $each; done | sort -n))


res=10000001
for ((i=0; i<N-1; i++))
    do
        current=${tab[$i]}
        next=${tab[$i+1]}
        delta=$((next-current))
        if [ $delta -lt $res ]; then
            res=$delta
        fi
    done

echo "$res"