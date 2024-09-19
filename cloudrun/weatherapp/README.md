# Google Cloudrun

### JSON viewer - [JSON viewer](https://jsonformatter.org/json-viewer)

docker build -t gcr.io/solar-bolt-436013-g3/weatherapp .

docker run -dp 8080:8080 gcr.io/solar-bolt-436013-g3/weatherapp

docker push gcr.io/solar-bolt-436013-g3/weatherapp