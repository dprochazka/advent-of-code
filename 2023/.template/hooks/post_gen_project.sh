#!/bin/fish

set day_raw {{ cookiecutter.day }}
set cookie_name {{ cookiecutter.env_user_cookie }}

set day (math $day_raw)
set session "session=$$cookie_name"

if test $day -gt (date +%d)
    echo "Cannot fetch input from the future (dec $day_raw)"
    exit 1
end

curl --cookie $session https://adventofcode.com/2023/day/{$day}/input > input.txt
