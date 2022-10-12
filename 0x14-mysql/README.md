# MYSQL 

***Setup mysql maaster-Slave***
```
### ON master
-sudo ufw allow from replica_server_ip to any port 3306
-#bind-address            = 127.0.0.1
-server-id               = 1
-log_bin                       = /var/log/mysql/mysql-bin.log
-binlog_do_db          = tyrell_corp
-sudo systemctl restart mysql
```

```
***on amster***
 mysqldump -uroot --all-databases --master-data > masterdump.sql
  grep CHANGE *sql | head -1
   scp masterdump.sql 44.200.73.180:

***on slave***
CHANGE MASTER TO 
-MASTER_HOST='HOSTIP',
-MASTER_USER='REPLIAuSER',
-MASTER_PASSWORD='REPLICAuserPASSWORD';

mysql -uroot -p
-start slave;
-show status;

```