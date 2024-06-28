# Installs Flask and Werkzeug

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
