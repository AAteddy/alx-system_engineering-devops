# Automating Nginx server configuration using Puppet.

package { 'nginx':
  ensure  => 'installed',
}

file_line { 'install':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.github.com/AAteddy permanent;',
}

file { '/var/www/html/index.html':
  ensure  => 'Hello World!',
}

service { 'nginx':
  ensure   => 'running',
  enable   => true,
  require  => Package['nginx'],
}
