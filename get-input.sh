#!/bin/bash -e

day=${1}

curl \
  -X GET \
  -o input/day-${day} \
  -b "session=$SESSION" \
  "https://adventofcode.com/2023/day/${day}/input"

