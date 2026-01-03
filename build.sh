#/bin/bash

MAXENCE_PATH="myIAs/botMaxence.sync"
THANOS_PATH="localIAs/iaThanosSeed8752.sync"
DORYAN_PATH="myIAs/botDoryan.sync"

source ./bin/activate
python3 roll_for_the_milkyway.py "$MAXENCE_PATH" "$DORYAN_PATH"
