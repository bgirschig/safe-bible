# The [safe] Holy Bible

This is a re-implementation of [safe bible](https://github.com/bgirschig/safeBible), but as a
single page application

This change was made to solve a few problems with the initial implementation:
- Page reload issues
  - Settings have to reload everytime. This creates a 'glitch' on every page change
  - Over-reliance on localStorage: if a user has disabled local storage, he'd lose his
  settings on every page change
- Tracking uncertainties: Is this visit an actual pageview, or just one user with
  cookies disabled, changing page ?

## Deploment info
### Hosting
Website is deployed to
app-engine [smart culture](https://console.cloud.google.com/appengine?project=smart-culture) project,
on service [bible](https://console.cloud.google.com/appengine/versions?project=smart-culture&serviceId=bible)

### Analytics
Analytics are self-hosted at [matomo.bastiengirschig.com](matomo.bastiengirschig.com)

### Domain name
- App engine default url is https://bible-dot-smart-culture.ew.r.appspot.com/
- the public domain name is https://bible.artimproved.com ([admin panel](https://domains.google.com/registrar/artimproved.com#))
- Subdomains are routed to app engine services (thanks to dispatch.yaml, source code in 'art improved'):
  - [subdomain].artimproved.com => [subdomain]-dot-smart-culture.ew.r.appspot.com

### API
The SPA loads data from an 'API' that contains all the books data. For now, this API
is hosted on the same service as the frontend ('bible'), but we might want to deploy
it to its own service for better scaling

### Backend routes summary
- `/`: The app's html page. opengraph parameters depend on the 'verse' url param
- `/books`: (legacy naming) returns a json with app-level info:
  - *books*: the metadata for all the books
  - *highlights*: a list of highlights for the 'highlights' page
  - *labelMap*: a mapping between label ID and label name&color (consistent with shareImages)
- `/chapter/BOOK_ID/CHAPTER_ID`: returns the verse data for a chapter
- `/shareImage/<BOOK_ID>/<CHAPTER_ID>/<VERSE_ID>`: the share image for a specific verse.
- `/shareImage/<BOOK_ID>/<CHAPTER_ID?>`: the share image for a specific book / chapter.
- `/shareImage`: Default share image.
