# Data sources and preparation

Retrieved October 27, 2026 from the public course data site.

## Triathlon data

Source: https://webpages.charlotte.edu/mschuck1/classes/DTSC2301/Data/Ironman1819.csv

Context: https://isle.stat.cmu.edu/SCORE/ironman_triathlon/

`ironman_2018_2019.csv` retains `Year`, `SwimTime`, `BikeTime`, `RunTime`, and `OverallTime` for the 1,105 female Lake Placid finishers in the source file. Times are in minutes. No race rows were removed; names, bibs, ranks, and other unused fields were excluded. Overall time includes segment times and transitions. Finishers do not represent all starters.

## Class survey

Source: https://webpages.charlotte.edu/mschuck1/classes/DTSC2301/Data/DTSC2301FirstDaySurvey_Responses_Clean.csv

`survey_jobs_contacts.csv` retains only `CampusJob`, `OffCampusJob`, and `NumbContacts` from 67 responses. No timestamps or unrelated respondent fields are included. The notebook constructs `job = 1` when either job field is Yes, `job = 0` when both are No, and missing otherwise. Two responses are excluded from the comparison for missing or invalid required values, leaving 65. Boxplots retain observed outliers.

This convenience sample is not representative of all students. Descriptive group differences do not establish causation or statistical significance.

## Generated outputs

`model_comparison.csv` and `survey_group_summary.csv` are regenerated from the snapshots by running the notebook. The source snapshots remain unchanged by notebook execution.
