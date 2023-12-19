from tsfresh import extract_features
from tsfresh.feature_extraction import MinimalFCParameters
from tsfresh.utilities.dataframe_functions import roll_time_series
from tsfresh.utilities.distribution import ClusterDaskDistributor
import pandas as pd
from scipy.io import loadmat
import numpy as np
import os


def main():
    # to increase the processing speed in roll_time_series and extract_features
    os.environ['OMP_NUM_THREADS'] = "1"
    os.environ['MKL_NUM_THREADS'] = "1"
    os.environ['OPENBLAS_NUM_THREADS'] = "1"

    my_df = pd.DataFrame()

    directories = {"normal-baseline-data"}  #
    for directory in directories:  #
        for sub_dir in os.listdir(directory):  # read the files separately
            sub_dir_path = os.path.join(directory, sub_dir)  #
            for file_name in os.listdir(sub_dir_path):  #
                file_path = os.path.join(sub_dir_path, file_name)
                # load matlab time series data to dictionary
                # and access the values associated with the first key, which is drive end data
                my_dict = loadmat(file_path)
                drive_end_array = np.array(list(my_dict.values())[3])

                # make an ID column array in which numbers 1 to 1000 will repeat 100 times each
                x = int(len(drive_end_array) / 1000)
                y = 1000 + (1000 // x) + 1
                alist = []
                for i in range(y):
                    for j in range(x):
                        alist.append(i + 1)
                my_arr = np.array(alist, dtype=int)
                df = pd.DataFrame({'sensor_data': drive_end_array.flatten()})
                df['id'] = my_arr[:len(drive_end_array)]

                # use rolling time series to increase the amount of data
                df_rolled = roll_time_series(df, column_id='id', min_timeshift=50)

                # feature extraction with minimal FC parameters to reduce the running time and memory usage
                feat = extract_features(df_rolled, column_id='id', column_sort='sort', column_value='sensor_data',
                                        default_fc_parameters=MinimalFCParameters())

                # apply labels for model training
                if directory == 'normal-baseline-data':
                    feat['y'] = 'normal'
                else:
                    feat['y'] = file_name[9:-2]

                # append the dataframe with extracted features
                my_df._append(feat)


if __name__ == "__main__":
    main()
