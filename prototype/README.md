# ResCounter - Python prototype
This is an early prototype for counting number of days spent outside UK and how many days can be spent outside UK at any time.

## Setting up application
1. Create a virtual environment with `python -m venv venv`.
2. Activate virtual environment using `source ./venv/bin/activate` in Unix environments, or `.\venv\Scripts\activate` on Windows.
3. Install dependencies using `pip install -r requirements.txt`.

## Running application
1. Prepare CSV file with your trips as shown in `infile.csv` example.
2. Activate virtual environment as in step 2 of the previous part.
3. Run `rescounter.py infile.csv` (replace `infile.csv` with your name of the input file).