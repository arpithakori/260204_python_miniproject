# Currency Converter
## Introduction about the project

Currency Converter is an application where one can convert their currency to the desired currency. For example people from India can convert their currency (INR) to any other currency like USD, YEN etc. Its very easy to just choose the currency from which one is converting to the required currency. 
Its very important to note that the exchange rates are changing almost every minute, for example 1 USD doesnt always equals to 70 INR. So my application here collects the real time exchange rates online so that the user gets the exact exchange rates.

## Functions of the Currency converter

User is able to select the currency they want to convert from.
User is able to select the currency they want to convert to.
When the convert button is clicked the conversion of the currency is done.
User is able to get the detials of the exchange rates on that particular day.
(example of text file - https://github.com/arpithakori/260204_python_miniproject/blob/master/2021-04-30.txt)

## Pre-requisites to run the files

1) Python version - 3.9.4
To download the latest version of python visit - https://www.python.org/downloads/

2) Downloading required packages
The packages used are:
* pip - 21.1.1
* future - 0.18.2
* EasyTkinter - 1.1.0
* requests - 2.25.1
* regex - 2021.44
* pytest - 6.2.3
The packages which are pre-installed in the pycharm IDE
* atomicwrites - 1.4.0
* attrs - 20.3.0
* certifi - 2020.12.5
* chardet - 4.0.0
* colorama - 0.4.4
* idna - 2.10
* iniconfig - 1.1.1	
* packaging -	20.9
* pluggy - 0.13.1
* py - 1.10.0	
* pyparsing - 2.4.7	
* setuptools - 56.0.0
* toml - 0.10.2	
* urllib3 - 1.26.4

These packages can be downloaded easily in pycharm as : 
* Settings => Project:your_project_name => Project Interpreter => + sign => Search for the packages you want to install

## How to run the project in pycharm IDE

1) Download the zip folder of the code
2) Install all the pre-requisites
3) The main file is - currency_converter.py - run this in the pycharm IDE
Press the run button to run the file or type python currency_converter.py in the pycharm command prompt
4) The GUI will be displayed to enter the values

## Pytest

Make sure that pytest is installed and in the pycharm IDE :
* Navigate to - Settings => Tools => Pycharm Integrated Tools => Default test runner => select pytest

1) The files - files_test.py and dict_test.py are for pytest
2) Run the files separately 

## Implementation of the Project

1) When the code is run in the pycharm IDE, the gui is displayed:

![run](https://github.com/arpithakori/260204_python_miniproject/blob/master/Run.png)

2) The clear view of GUI:

![gui](https://github.com/arpithakori/260204_python_miniproject/blob/master/GUI%20Initial.png)

3) User can select among the countries for exchange rates:

![select](https://github.com/arpithakori/260204_python_miniproject/blob/master/select.png)

4) User can enter the values of the rates they want to convert:

![enter](https://github.com/arpithakori/260204_python_miniproject/blob/master/enter.png)

5) A pop arises if we do not enter any values in the boxes specified:

![pop](https://github.com/arpithakori/260204_python_miniproject/blob/master/pop.png)

6) To exit the application, user can click the exit button
