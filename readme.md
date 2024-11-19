##Requirements

pip3 install flask mysql-connector-python

#need to open port 5000 for flask
sudo systemctl status firewalld
sudo firewall-cmd --permanent --add-port=5000/tcp
sudo firewall-cmd --permanent --add-port=5000/udp
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports

#If you want to add the rule to a specific zone (e.g., public), specify the zone:

sudo firewall-cmd --zone=public --permanent --add-port=5000/tcp


#Ensure your Flask app is running with host="0.0.0.0" to allow external connections:
#app.run(host="0.0.0.0", port=5000)


#create service
cp user_app.service /etc/systemd/system/   #copy service file to systemd
touch /var/log/python_app.log   # create log file
systemctl daemon-reload
systemctl start user_app.service
