from schematics.models import Model
from schematics.types import FloatType
from schematics.types import StringType

class Features(Model):
    """All extracted features: general, time, users.
    """

    general_female_websitescore = FloatType()

    general_male_websitescore = FloatType()

    time_extract_weekend = FloatType()

    time_extract_daytime = StringType()

    user_avg_no_of_sitevisits_per_day = FloatType()

    user_no_of_sitevisits = FloatType()

    user_extract_time_between_sessions = FloatType()

    user_extract_avg_time_per_page = FloatType()
