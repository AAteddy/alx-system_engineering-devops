# Installs flask version 2.1.0 from pip3.
package { 'flask', 'Werkzeug':
  ensure   => '2.1.0',
  provider => 'pip3',
}
