#!/bin/bash
# send JSON POST req to URL
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
