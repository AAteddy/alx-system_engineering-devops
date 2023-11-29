# Automating Nginx server configuration using Puppet.

package { 'nginx':
  ensure  => installed,
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

exec { 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\treturn 301 https:\/\/github.com\/AAteddy\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider  => shell,
}

service { 'nginx':
  ensure   => running,
  require  => Package['nginx'],
}
