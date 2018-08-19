Gender classification
=============================

Backend for a gender classifier

Dependencies
------------

* Python >= 3.5, virtualenv
* Make

Feature Extraction
------------

The Backend first calculated the defined general, 
time and user features of a given dataset of surfing
behavior of users.

general features:
The main features are a female and a male website
score based on tf-idf features from surf behavior
from registered users.

time features:
This features checks wheter users tend to visit the
web page on weekend or during which part of the 
day e.g. in the morning or late at night.

user features:
Here we calculate e.g. the avg time of
how long a user visit an url. 


It's easy to extend new features or remove them
to the algorithm by adding new feature methods,
that can also easily be procesed in parallel
in one loop.
Keep in mind to change the feature model which
validates a giving feature set.

Classification
------------

After feature extraction we can easily train
a classifier a the jupyter notebook.

As the given test data set does not contain
any information about the gender of a user
we split the trainings set into a train and
validation set to evalute the classifier performance
a TSNE-plot helps to visualize the data set
for a more intuitive evaluation.

gender predictions live in etc/csv/user_gender_predictions.csv


Building
--------

To **build** the project run:
::
    make

Start feature extractor
--------

To **start** the feature extractor run:
::
    make start

Note: before starting the feature extractor
add the train.csv and test.csv into the
folder etc/csv/

Open the jupyter notebook
--------
To **start** the jupyter notebook run:
::

jupyter notebook gender_dataset.ipynb

Testing
-------

Not implemented yet

Limitations and future work
-------

Not implemented yet
