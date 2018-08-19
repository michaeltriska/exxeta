# -*- coding: utf-8 -*-
from .helpers import cast_response_to_int
from functools import reduce
import heapq


class GeneralFeaturesExtractor:

    def __init__(self):
        """listing of all the feature methods here,
           so that they can easily be procesed in
           parallel in one loop.
        """
        self.methods = {
            "general_female_websitescore":
                self.extract_female_websitescore,

            "general_male_websitescore":
                self.extract_male_websitescore
        }

    def extract_features(self, events, tdm):
        """ Iterates over all configured methods
            saves the results in the dictionary
            with the keys.
        """
        results = {
            key: method(
                events, tdm)
            for key, method in self.methods.items()
        }
        return results

    @cast_response_to_int
    def extract_female_websitescore(self, events, tdm):
        scores = [tdm.loc[i].f for i in events['path']]
        scores = heapq.nlargest(3, scores)
        return reduce(lambda x, y: x * y, scores)

    @cast_response_to_int
    def extract_male_websitescore(self, events, tdm):
        scores = [tdm.loc[i].m for i in events['path']]
        scores = heapq.nlargest(3, scores)
        return reduce(lambda x, y: x * y, scores)
