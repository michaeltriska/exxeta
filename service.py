from gender_classification.modules.tdm_calculator import TDM_Calculator
from gender_classification.core.preprocessor import EventPreprocessor
import pandas as pd


if __name__ == "__main__":

    def func():

        ep = EventPreprocessor()

        print("loading data")
        df_train = pd.read_csv(
            'etc/csv/train.csv', sep=',', index_col=None)
        df_test = pd.read_csv(
            'etc/csv/test.csv', sep=',', index_col=None)

        print("calculate term document matrix")
        tdmc = TDM_Calculator()
        tdm = tdmc.extract_features(df_train)

        print("extract training features")
        df_train_usergroup = df_train.groupby('user_id')
        i = 0
        trainings_set = []
        for user, user_events in df_train_usergroup:
            if user:
                events = ep.preprocess_event(user_events, tdm)
                events['user'] = user
                events['gender'] = user_events['gender'].iloc[0]
                trainings_set.append(events)
                i = i + 1
                if i == 3500:
                    pd.DataFrame(trainings_set) \
                        .to_csv('etc/notebooks/data/train.csv', sep=',')
                    break

        print("extract test features")
        df_test_usergroup = df_test.groupby('user_id')
        test_set = []
        for user, user_events in df_test_usergroup:
            if user:
                events = ep.preprocess_event(user_events, tdm)
                events['user'] = user
                test_set.append(events)
        pd.DataFrame(test_set) \
            .to_csv('etc/notebooks/data/test.csv', sep=',')

    func()
