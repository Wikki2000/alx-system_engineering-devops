-- Create replica user.
CREATE IF NOT EXISTS USER 'replica_user'@'%' IDENTIFIED BY "your_password"

-- Grant replication priviledge on all db in in primary server.
-- To read the bin-log and update the replica server
GRANT REPLICATION SLAVE ON *.* ON TO 'replica_user'@'%' 
