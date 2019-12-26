# ResCounter - Python prototype
This is an early prototype an app helping immigrants maintain `continuous residence` in the UK.
It should be useful for planning trips and stays abroad, while making sure the HM Government's residency requirements for [`Settled Status`](https://www.gov.uk/settled-status-eu-citizens-families/what-settled-and-presettled-status-means) or [`Indefinite Leave to Remain`](https://www.gov.uk/government/publications/indefinite-leave-to-remain-calculating-continuous-period-in-uk) are met.

## No warranty
The author of the application takes no responsibility for any inaccurate information provided by the application.
Application is supposed only to provide aid to those determining length of their residency in the UK.
Application cannot be used to make any claims with HM Government institutions.

## Setting up application
1. Create a virtual environment with `python -m venv venv`.
2. Activate virtual environment using `source ./venv/bin/activate` in Unix environments, or `.\venv\Scripts\activate` on Windows.
3. Install dependencies using `pip install -r requirements.txt`.

## Running application
1. Prepare CSV file with your trips as shown in `infile.csv` example.
2. Activate virtual environment as in step 2 of the previous part.
3. Run `rescounter.py infile.csv` (replace `infile.csv` with your name of the input file).

## Reading output
Table provided in the output shows trips provided in the input, as well as additional information computed by the app.

For each row:
* Column `time out of UK` shows how many days you spent outside the UK  within a year before the arrival date.
* Column `allowable absence` shows number of days you could spend outside the UK without violating `continuous residence` requirement within a year before the arrival date.

## Allowable absence
HM Government websites sometimes define `continuous residency` as `at least 6 months in any 12 month period`, other times as `180 days allowable absence in the continuous 12-month period`.
As 180 days is shorter than 6 months (182.5-183 days), this app uses 180 days as a safer bet.