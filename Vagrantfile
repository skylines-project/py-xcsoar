$script = <<SCRIPT

set -e

# set environment variables

cat >> ~/.profile << EOF
export LANG=C
export LC_CTYPE=C
export USE_CCACHE=y
EOF

# adjust apt-get repository URLs

sudo bash -c "cat > /etc/apt/sources.list" << EOF
deb mirror://mirrors.ubuntu.com/mirrors.txt precise main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-security main restricted universe multiverse
EOF

# update apt-get repository

sudo apt-get update

# install base dependencies

sudo apt-get install -y --no-install-recommends \
    g++ pkg-config libcurl4-openssl-dev libfreetype-dev libpng-dev python-dev ccache git

# install pip

wget -N -nv https://bootstrap.pypa.io/get-pip.py
sudo -H python get-pip.py

# install dev dependencies

cd /vagrant
sudo -H pip install -r requirements.txt

SCRIPT

Vagrant.configure("2") do |config|
  # TravisCI uses a Precise Pangolin base image
  config.vm.box = 'ubuntu/precise64'

  config.vm.network 'private_network', type: 'dhcp'
  config.vm.synced_folder '.', '/vagrant', type: 'nfs'

  config.vm.provider 'virtualbox' do |v|
    host = RbConfig::CONFIG['host_os']

    # Give VM 1/4 system memory & access to all cpu cores on the host
    if host =~ /darwin/
      cpus = `sysctl -n hw.ncpu`.to_i
      # sysctl returns Bytes and we need to convert to MB
      mem = `sysctl -n hw.memsize`.to_i / 1024 / 1024 / 4

    elsif host =~ /linux/
      cpus = `nproc`.to_i
      # meminfo shows KB and we need to convert to MB
      mem = `grep 'MemTotal' /proc/meminfo | sed -e 's/MemTotal://' -e 's/ kB//'`.to_i / 1024 / 4

    else
      cpus = 2
      mem = 1024
    end

    v.customize ['modifyvm', :id, '--memory', mem]
    v.customize ['modifyvm', :id, '--cpus', cpus]
  end

  config.vm.provision 'shell', inline: $script, privileged: false
end
