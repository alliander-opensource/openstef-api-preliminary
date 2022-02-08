Example data
============

The data is this directory (`./data`) is for illustration purposes only.
In a real application your data will probably be served from some database.

Remove this directory from your application and remove this line copying the data from the `Dockerfile`:
```Dockerfile
COPY ./data ./data
```

BASE_URL="https://icarus-openstf-api-icarus-prd.appx.cloud/api/v1"
BASE_URL="http://127.0.0.1:8000/api/v1"

curl -X 'POST' \
  '$BASE_URL/forecasts/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '@./data/307_generate_forecast_input_2021-05-17_2021-06-03.json'

curl -X 'POST' \
  "$BASE_URL/forecasts/generate" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '@./data/307_generate_basecase_forecast_input_2021-05-17_2021-06-03.json'

curl -X 'POST' \
  '$BASE_URL/trained-models/train' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '@./data/307_train_model_input_2021-03-02_2021-05-31.json'

curl -X 'POST' \
  "$BASE_URL/hyperparameters/optimize" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '@./data/307_optimize_hyperparameters_input_2021-03-02_2021-05-31.json'