# data-processing-with-pyspark-and-mongodb
Big Data Processing with PySpark and MongoDB

## Overview 

This is Proof of Concept for creating a Data Pipeline with PySpark and MongoDB.

## Use Case

Process a large dataset from NOAA (National Oceanic and Atmospheric Administration) showing precipitation rates for a 10 year period from US state of Wisconsin.

## Architecture

![Architecture](https://github.com/user-attachments/assets/7e06f4e1-7de7-4f5e-9faf-2fee2b6956a4)

## Tech Stack

- Apache Spark
- MongoDB (Community Edition)
- Python
- PowerBI Desktop

## Dataset

Dataset from NOAA (National Oceanic and Atmospheric Administration) showing precipitation rates for a 10 year period from US state of Wisconsin.

## Solution

PySpark code will extract / read the data from NOAA csv file into a Spark dataframe. Then data will be cleansed in such a way that invalid records where precipitation rate is 999.99 will be discarded. Then valid records are being inserted / saved into a collection in MongoDB database. Also individual records are being grouped by station names so that a report can be generated on what are the top 5 stations where precipitation frequency was highest. Further this grouped / processed data is also being saved / inserted to a seperate MongoDB collection.

## Visualization

![Visualization](https://github.com/user-attachments/assets/280216c8-0668-4c83-a769-8b4c0ada877e)

## Limitations / Improvement Areas

Due to ODBC driver issue meant to connect PowerBI with MongoDB, PowerBI couldn't import data directly from MongoDB. As a workaround, exported data from MongoDB collection into a CSV file which PowerBI consumed as a data source for creating visualization.

