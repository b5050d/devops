#!/bin/bash

cd /home/b5050d/Workspace/portfolio || exit 1

git remote update

LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})
BASE=$(git merge-base @ @{u})

if [ "$LOCAL" = "$REMOTE" ]; then
        echo "Repo up to date"
elif [ "$LOCAL" = "$BASE" ]; then
        echo "Pulling changes"
        git pull
        # installing any new packages for prod
        /home/b5050d/Workspace/portfolio/venv/bin/pip install -r requirements.txt
        sudo systemctl restart portfolio
elif [ "$REMOTE" = "$BASE" ]; then
        echo "Local is ahead of remote"
else
        echo "Diverged - manual intervention needed"
fi