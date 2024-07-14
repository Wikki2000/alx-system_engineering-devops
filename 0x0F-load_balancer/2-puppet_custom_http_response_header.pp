exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec { 'install':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'X-Served-By':
  command  => 'sudo sed -i "/listen 80 default_server;/a         add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'service -y nginx':
  command => '/usr/sbin/service nginx restart',
}
