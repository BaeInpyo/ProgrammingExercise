time ./a.out < input.txt > vip_result.txt
echo "vip finished"
time python sjw_christmas.py < input.txt > sjw_result.txt
echo "sjw finished"
diff vip_result.txt sjw_result.txt

