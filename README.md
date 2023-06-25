# Helping the Homies

## Running the Test
### Create virtual python environment:
`python -m venv venv`

### Activate virtual environment:
Linux/Mac - `source venv/bin/activate`
Windows - `venv\Scripts\activate`

### Install dependencies
`pip install -r requirements.txt`

### To run the test just simply run following command to the terminal:
`pytest`

### To run parallel tests (4 is basically the amount test to run concurrently):
`pytest -n 4`

## Run on a a docker container
Build container
`docker build -t my_container .`

Run container
` docker run -d -v $(pwd)/test_results:/app my_container`

After running the container, the test_results folder should now have the `report.html` file which you can open and view the reports