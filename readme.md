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

<img width="1076" alt="Screenshot 2024-11-19 at 11 14 51 AM" src="https://github.com/user-attachments/assets/b7504d97-58de-424f-8070-5b2e091da1e7">
