# move to this file's directory
cd "$(dirname "$0")"

# build
cd frontend
npm run build

# deploy
cd ../app-engine
gcloud app deploy --project smart-culture --account bastien.girschig@gmail.com --quiet