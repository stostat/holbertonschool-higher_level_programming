#!/bin/bash
# Takes URL displays all HTTP methods the server will accept.
curl -sI "$1" | grep 'Allow' | cut -b8-
