git init
git add .
git commit -m "$(date '+%H:%M:%S - %d/%m/%Y')"
git branch -M main
git remote add origin https://github.com/anaksubuh/kosku.git
git push -u origin main
