export default {
  host: 'https://matomo.bastiengirschig.com',
  siteId: 2,
  debug: false,

  // Enables link tracking on regular links. Note that this won't
  // work for routing links (ie. internal Vue router links)
  enableLinkTracking: true,

  enableHeartBeatTimer: false,
  heartBeatTimerInterval: 15,

  // Tell Matomo the website domain so that clicks on these domains are not tracked as 'Outlinks'
  // Default: undefined, example: '*.example.com'
  domains: 'bible.artimproved.com',
};
