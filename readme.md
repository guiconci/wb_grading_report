# Raw Material Needed consolidation
This app was created to fill a simple need, make a report that takes all data from a long plan. The supervisor had issues reading the schedule and calculating due to the ammount of data and unecessary manual work.
The app was initially hosted on heroku and had schedule redeployment for 1h so would catch the new table updated in the morning.
It solved a big problem with a simple solution.

## Features
* Allows user to copy paste from an existing plan into a google sheets spreadhseet.
* * Plan is defined for two days.
* Report builds a table showing the needed amounts for each grade per day.
* * Along with the percentages of the total, which allowed also choosing the correct raw materials to sort based on historical outcome per supplier.
* Report could be accessed through the internet and mobile phone

## How to run locally
* Install python
* Clone repository
* Then activate virtual env
* Install dependencies
* Run the app
```bash
python3.11 -m venv venv
git clone https://github.com/guiconci/wb_grading_report
venv\Scripts\activate
pip install numpy==1.26.4
python final_report.py
```
* You should see the message:
* * Dash is running on http://127.0.0.1:8050/
