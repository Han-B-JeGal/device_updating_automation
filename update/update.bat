for /f "delims=" %%i in (ip.txt) do scp -r C:\update root@%%i:/root/sensor
timeout 1
for /f "delims=" %%i in (ip.txt) do plink -batch -ssh root@%%i -pw we@bless chmod 777 /root/sensor/update/update.sh
timeout 1
for /f "delims=" %%i in (ip.txt) do plink -batch -ssh root@%%i -pw we@bless /root/sensor/update/update.sh
timeout 1
