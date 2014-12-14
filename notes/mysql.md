### install mySQL on ubuntu
```
sudo apt-get purge mysql-client-core-5.5
sudo apt-get install mysql-server
sudo apt-get install mysql-client
\\check mysql status
sudo netstat -tap | grep mysql
\\restart mySQL
sudo /etc/init.d/mysql restart
\\configuration files
/etc/mysql/my.cnf
```

### how to access MySQL shell
```
mysql -u root -p
```



[googd reference](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
