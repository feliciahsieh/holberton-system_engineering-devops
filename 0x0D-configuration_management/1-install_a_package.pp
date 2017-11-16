# Puppet file to install puppet-lint

package { 'puppet-lint -v 2.1.1' :
  ensure => 'installed',
}
