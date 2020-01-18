# WSDM - KKBox's Churn Prediction Challenge

>KKBOX is Asia’s leading music streaming service, holding the world’s most
>comprehensive Asia-Pop music library with over 30 million tracks.
>They offer a generous, unlimited version of their service to millions of
>people, supported by advertising and paid subscriptions. This delicate
>model is dependent on accurately predicting churn of their paid users. (...)
>
>In this challenge, you are asked to predict whether a user will churn
>after his/her subscription expires. (...)


Source: [Kaggle Competition](https://www.kaggle.com/c/kkbox-churn-prediction-challenge/overview)


## Project description

> **What Is Customer Churn?**

> Customer churn is the percentage of customers that stopped using your company's product or service during a certain time frame.

[Source](https://blog.hubspot.com/service/what-is-customer-churn)


The goal of this project is to predict whether or not a user
will leave the music streaming service after their subscription expires.


### Requirements

This project was written in Python 3.8. In order to set up and use a conda environment
with all the required packages, you can run:
```
conda env create -f conda_env.yml
conda activate churn-prediction
```

## Dataset

Data used for this project can be found at [the competition's page](https://www.kaggle.com/c/kkbox-churn-prediction-challenge/data).
(As the CSV files are quite large, they are not a part of this repository).

In order to decrease memory requirements, I decided to consider only a part of the original dataset.

### Files used

The following file names correspond to the data from Kaggle's website:

* `members_v3.csv`
* `sample_submission_v2.csv`
* `train_v2.csv`
* `transactions_v2.csv`

In order to run the scripts correctly, the data should be downloaded
and located in `data/` directory, with their names unchanges.
(Since the default download file format is compressed, they should be extracted
  to plain CSVs first.)
