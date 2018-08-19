from gender_classification.features.time import TimeFeaturesExtractor
from gender_classification.features.user import UserFeaturesExtractor
from gender_classification.features.general import GeneralFeaturesExtractor
from gender_classification.models.features import Features

class EventPreprocessor:
    """Facade in front of all the feature extractors. It calls the
    'extract_feature' method for every feature extractor and then
    merges all the features to one dict, that should have the following
    structure:
    {
       "time_feature1_name": ...,
       "time"_feature2_name": ...,
       "user_feature1_name": ...
       and so on
    }
    """

    def __init__(self):

        self.time_features_extractor = TimeFeaturesExtractor()
        self.user_features_extractor = UserFeaturesExtractor()
        self.general_features_extractor = GeneralFeaturesExtractor()

    def preprocess_event(self, event, tdm):
        # extract time features
        time_features = self.time_features_extractor \
                            .extract_features(event)
        user_features = self.user_features_extractor \
                            .extract_features(event)
        general_features = self.general_features_extractor \
                               .extract_features(event, tdm)

        # merge all features into one dict
        all_features = {
            **time_features,
            **user_features,
            **general_features}

        Features(all_features).validate()
        return all_features
