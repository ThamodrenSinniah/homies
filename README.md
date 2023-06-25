
# Helping the Homies  
  
## Running the Test  
### Create virtual python environment:  
`python -m venv venv`  

> You create virtual environment in Python because when you install all
> the various dependencies, you want to install for this current
> project. Without virtual environments, you will be installing them on
> your machine and it will be accessible to ALL projects. This is bad
> because now you're wasting space by having redundant dependencies on
> projects that don't even need it.

  
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

### Build container

`docker build -t my_container .`  
  
### Run container  
`docker run my_container`  
  
## Getting reports
After the docker finishes its test, you can copy the `report` folder in the container.
The following line will copy the folder directory
`docker cp <container_id>:/app/report .`

Now you should be able to see the `report` folder on your current working directory

## Notes
### Default to Firefox

I used Firefox because I do not need to install a driver and add it to my working directory unlike Chrome. If you want to do so, you always can. But remember that you would need to change the browser to `Chrome` in `tests/fixtures/browser.py`. The container would also not work because it only has Firefox. Feel free to install Chrome by adding a command to the `Dockerfile`.

### Headless
Running a test on headless basically mean the browser will be running in the background and won't show any UI. Meaning you don't actually see the browser opening up and clicking and inputting. If you want to disable this, you can do so by removing the `options.add_argument('--headless')` line of code in `tests/fixtures/browser.py`
