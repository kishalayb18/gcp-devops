# gcp-devops
GCP DevOps related projects will be here


docker build -t gcr.io/solar-bolt-436013-g3/weatherapp .

docker run -dp 8080:8080 gcr.io/solar-bolt-436013-g3/weatherapp

docker push gcr.io/solar-bolt-436013-g3/weatherapp