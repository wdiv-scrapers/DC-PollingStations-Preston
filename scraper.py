from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


stations_url = "http://maps.preston.gov.uk/electionsdemocracyclub/wfs.exe?service=WFS&version=2.0.0&request=GetFeature&typeNames=ns%3APolling_Stations&outputFormat=application%2Fvnd.geo%2Bjson"
districts_url = "http://maps.preston.gov.uk/electionsdemocracyclub/wfs.exe?service=WFS&version=2.0.0&request=GetFeature&typeNames=ns%3APolling_District_Boundaries&outputFormat=application%2Fvnd.geo%2Bjson"
council_id = 'E07000123'


stations_scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = RandomIdGeoJSONScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
