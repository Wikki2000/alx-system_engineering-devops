# Ensured nginx package is installed
package { 'nginx':
    ensure    => installed
}

# Define content for root
file { '/var/www/html/index.html':
    content    => 'Hello World!',
    ensure     => install,
}

# Configure Nginx default site
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  root /var/www/html;
  index index.html index.htm;

  location /redirect_me {
    return 301 https://youtube.com/;
  }

  error_page 404 /404;
  location /404 {
    internal;
    root /var/www/html;
  }
}
",
}

# Enable default site by creating a symlink
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
} 
