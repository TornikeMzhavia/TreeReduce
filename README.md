# Tree structure simplifier

Program gets as an input tree of data consisting of redundant duplicates.

This data holds the information about list of technologies used on each level of hierarchy.

As an output a deduplicated and compressed tree is presented.

## Prerequisites

* Python 3 is needed to run this appllication.
* Activate the 'venv' virtual environment. (More info [here](https://docs.python.org/3/tutorial/venv.html))
* Install the required packages from the **requirements.txt** file by running
```
pip install -r requirements.txt
```
* File with input data formatted the following way

```
url1 -> technology1, technology2 ...
url2 -> ...
...
...
```

## Running the application

Simply call the **run.py** file from the command prompt.
Configuration can be set in **config.ini**.

```
run.py
```

## Setting up the configuration

* **input_directory** - path of the file containing the input tree in the correct format
* **output_directory** - path for the output file to be created
* **split_symbol** - Input format specifier. The default is set to '->'. Others can be used
* **element_separator** - Input format specifier. The default is set to ','. Others can be used

## Author

* **Tornike Mzhavia** - [LinkedIn](https://www.linkedin.com/in/tornike-mzhavia/)
