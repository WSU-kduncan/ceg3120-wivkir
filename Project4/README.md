## Setup Load Balancing TODOs

Setup the following and add documentation or screenshots to your `README.md` file as specified.

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs.
   - Description of how file is configured
     - Each entry is set up like this
```
#Server 2 (Description of connection)
        Host S2 (alias to use for ssh)
        HostName 10.0.1.12 (ip to connect to)
        User ubuntu (user on system being logged into)
        IdentityFile /home/ubuntu/.ssh/Server2.pem (location of private key)
```

2. Document how to SSH in between the systems utilizing their private IPs.
   - Once set up in the config file, just type 'ssh S2'('ssh Host').
3. How to set up a HAProxy load balancer
   - What file(s) where modified & their location
     - etc/haproxy/haproxy.cfg was modified
   - What configuration(s) were set (if any)
     - the frontend and backend settings were change to make haproxy now listen on port 80 and send traffic to either of the backend servers
   - How to restart the service after a configuration change
     - sudo systemctl restart haproxy
   - Resources used (websites)
     - https://www.vultr.com/docs/how-to-install-haproxy-on-ubuntu-20-04/
4. How set up a webserver
   - What file(s) were modified & their location
     - /etc/apache2/ports.conf
     - /etc/apache2/sites-available/000-default.conf
   - What configuration(s) were set (if any)
     - in port.conf, the first listen, 'Listen 80', was changed to 'Listen 8080'
     - in 000-default.conf the first VirtualHost, '<VirtualHost *:80>', was changed to '<VirtualHost *:8080>'
   - Where site content files were located (and why)
     - /var/www/html/index.html, because thats where apache look for them first
   - How to restart the service after a configuration change
     - sudo systemctl restart apache2
   - Resources used (websites)
     - https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
     - https://www.vultr.com/docs/how-to-install-haproxy-on-ubuntu-20-04/
5. From the browser, when connecting to the proxy server, take two screenshots.
   - I honestly waited until Thursday to start this project, thinking about 6 hours in one day would be enough to get it working. 
   - Unfortunately, I did not give myself enough time to complete the project. Although I finished the rest of it in about 4 hours and have been troubleshooting one issue for another 4.
   - I could not figure how to get apache to communicate to the haproxy that it was running. Port 8080 was open and listening on both back-end servers. The front-end server was listening on port 80 and round robin forwarding to port 8080 on the backend. I kept getting "Server web_servers/server-1 is DOWN, reason: Layer4 connection problem, info: "No route to host"". Google suggested it was a firewall issue, so I adjusted the security group to allow traffic into and out of port 8080. When that did'nt work I tried changing the iptables to allow port 8080 access. That also didn't work. Eventually I decided to try changing the ufw and locked myself out. 
   - I know I won't get credit for this portion. I just wanted a record of what happended. Also, it felt wrong to leave the photo area blank when I spent so long trying to get them.
