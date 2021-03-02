rm -rf /root/recvSensorData
rm -f /opt/recv_data
rm -f /root/sensor/db/models.py
rm -f /root/sensor/main.py
mkdir /root/recvSensorData
mv /root/sensor/update/createtable.py /root/sensor
mv /root/sensor/update/authrized_keys /root/.ssh
mv /root/sensor/update/main.py /root/sensor
mv /root/sensor/update/recvSensorData/Makefile /root/recvSensorData
mv /root/sensor/update/recvSensorData/recv_data /root/recvSensorData
mv /root/sensor/update/recvSensorData/recv_data.c /root/recvSensorData
mv /root/sensor/update/recvSensorData/recv_data.service /root/recvSensorData
mv /root/sensor/update/tcp_socket_client_sync.py /root/sensor
mv /root/sensor/update/models.py /root/sensor/db
mv /root/sensor/update/data_delete_day.py /root/sensor
mv /root/sensor/update/data_delete_month.py /root/sensor
chmod 755 /root/recvSensorData/recv_data
cp /root/recvSensorData/recv_data /opt
cp /root/recvSensorData/recv_data.service /etc/systemd/system
systemctl daemon-reload
systemctl enable recv_data
systemctl start recv_data
rm -r /root/sensor/update
reboot
