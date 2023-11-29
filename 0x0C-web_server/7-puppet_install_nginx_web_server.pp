# Automating Nginx server configuration using Puppet.

package { 'nginx':
  ensure => 'installed',
}


file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  mode    => '0644',
  require => Package['nginx'],
}

exec { 'append_redirect_me':
  command => "/usr/bin/sed -i '/^}$/i \\\n\tlocation \\/redirect_me {return 301 https:\\/\\/www.github.com\\/AAteddy;}' /etc/nginx/sites-available/default",
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
