# -*- coding: utf-8 -*-
from .helpers import cast_response_to_int
import pandas as pd
pd.options.mode.chained_assignment = None

class TimeFeaturesExtractor:

    def __init__(self):
        """listing of all the feature methods here,
           so that they can easily be procesed in
           parallel in one loop.
        """
        self.methods = {
            "time_extract_weekend":
                self.extract_weekend,
            "time_extract_daytime":
                self.extract_daytime
        }

    def extract_features(self, events):
        """ Iterates over all configured methods
            saves the results in the dictionary
            with the keys.
        """
        events['timestamp'] = \
            pd.to_datetime(events['timestamp'])
        events['day_of_week'] = \
            events['timestamp'].apply(lambda d: d.dayofweek)
        events['day_of_year'] = \
            events.timestamp.dt.dayofyear
        events = \
            events.groupby(['day_of_year']).first()

        results = {
            key: method(
                events)
            for key, method in self.methods.items()
        }
        return results

    @cast_response_to_int
    def extract_weekend(self, events):
        events['weekend'] = \
            events['day_of_week'] \
            .apply(lambda d: False if d < 5 else True)
        return round(float(events['weekend'].mean()), 2)

    @cast_response_to_int
    def extract_daytime(self, events):
        events['hour'] = events['timestamp'].apply(lambda d: d.hour)
        hour_bins = [-1, 5, 11, 16, 21, 23]
        bin_names = ['late_night', 'morning', 'afternoon', 'evening', 'night']
        events['time_of_day_bin'] = \
            pd.cut(
                events['hour'],
                bins=hour_bins,
                labels=bin_names)

        return events['time_of_day_bin'].value_counts().idxmax()
