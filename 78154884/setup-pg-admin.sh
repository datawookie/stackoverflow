#!/bin/bash

cat <<EOT >> /var/lib/postgresql/data/postgresql.conf
shared_preload_libraries='/usr/share/postgresql/16/contrib/pldebugger/plugin_debugger.so'
EOT
