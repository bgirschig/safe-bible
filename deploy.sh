# move to this file's directory
cd "$(dirname "$0")"

# build frontend
cd frontend
npm run build

# pre-build books.json (disabled for now as it's not sure this is hlpful)
# cd ../app-engine
# source ./env/bin/activate
# python buildBooksJson.py

# deploy
cd ../app-engine
gcloud app deploy --project smart-culture --account bastien.girschig@gmail.com --quiet