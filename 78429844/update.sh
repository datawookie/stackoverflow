#!/bin/bash

URL=https://www.google.com

jq --arg url "$URL" '.defaultOptions.environmentVariableEntries += [{"key": "URL", "value": $url}]' json.xctestplan
