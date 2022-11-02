#!/bin/bash

tmux new-session -d -s elastic
tmux send-keys -t elastic:0 "cd elasticsearch*; ./bin/elasticsearch" Enter
tmux split-window -h

tmux send-keys -t elastic:0.1 "jupyter lab" Enter

tmux a -t elastic
