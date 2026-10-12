#!/bin/bash

current_time=$(date +"%H:%M")
current_hour=$(date +"%H")
current_minute=$(date +"%M")

end_hour=18
end_minute=0

remaining_minutes=$(( (end_hour * 60 + end_minute) - (current_hour * 60 + current_minute) ))

if [ "$remaining_minutes" -lt 0 ]; then
    remaining_minutes=0
fi

hours=$((remaining_minutes / 60))
minutes=$((remaining_minutes % 60))

echo "Current time: $current_time"
echo "Work day ends after $hours hours and $minutes minutes."
