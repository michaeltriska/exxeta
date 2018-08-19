# -*- coding: utf-8 -*-
from .helpers import cast_response_to_int
import pandas as pd
import numpy as np


class UserFeaturesExtractor:

    def __init__(self):
        """listing of all the feature methods here,
           so that they can easily be procesed in
           parallel in one loop.
        """
        self.methods = {
            "user_avg_no_of_sitevisits_per_day":
                self.extract_avg_no_of_sitevisits_per_day,
            "user_no_of_sitevisits":
                self.extract_no_of_sitevisits,
            "user_extract_avg_time_per_page":
                self.extract_avg_time_per_page,
        }

    def extract_features(self, events):
        """ Iterates over all configured methods
            saves the results in the dictionary
            with the keys.
        """
        results = {
            key: method(
                events)
            for key, method in self.methods.items()
        }
        return results

    @cast_response_to_int
    def extract_no_of_sitevisits(self, events):
        return len(events)

    @cast_response_to_int
    def extract_avg_no_of_sitevisits_per_day(self, events):
        events['day_of_year'] = events.timestamp.dt.dayofyear
        no_per_visit = [len(v) for _, v in events.groupby('day_of_year')]
        return sum(no_per_visit) / float(len(no_per_visit))

    @cast_response_to_int
    def extract_avg_time_per_page(self, events):
        events['delta'] = \
            (events['timestamp'] - events['timestamp'].shift()).fillna(0)
        events['delta_in_s'] = \
            events['delta'].dt.total_seconds()
        events['categories'] = \
            pd.cut(
                events['delta'],
                bins=[np.timedelta64(t, 's') for t in [0, 3600]])
        time_means = []
        for k, v in events.iterrows():
            if v.delta_in_s == 0 or v.delta_in_s > 3600:
                pass
            else:
                time_means.append(v.delta_in_s)
        return sum(time_means) / float(len(time_means))
