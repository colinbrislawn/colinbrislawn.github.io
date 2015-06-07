pelican content --output output --settings publishconf.py
cd output
git add --all
git commit -m "commit and push all"
git push origin master --force