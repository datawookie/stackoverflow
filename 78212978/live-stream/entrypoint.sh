#! /bin/bash

gcsfuse --foreground --key-file /service-account-key.json **** /ls_media &
nginx -g "daemon off;"
