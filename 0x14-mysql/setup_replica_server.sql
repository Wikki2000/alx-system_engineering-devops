STOP SLAVE; --Stop slave if was already running
CHANGE MASTER TO
    MASTER_HOST='your_ap adress',
    MASTER_USER='replica_user',
    MASTER_PASSWORD='repica_password', --- Replace this with the actual password u use for replica_user
    MASTER_LOG_FILE='mysql-bin.000003', -- replace with the File value from the SHOW MASTER STATUS
    MASTER_LOG_POS=921; -- replace with the Position value from the SHOW MASTER STATUS
START SLAVE;
