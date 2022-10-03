from datetime import datetime

import wget
import cdflib
import numpy as np


def download_data(date):
    """Donwloads NASA data."""

    for version in ['04', '03', '02', '01']:
        try:
            wind_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/mfi/mfi_h2/2022/wi_h2_mfi_{date}_v{version}.cdf'
            wind_filename = wget.download(wind_url)
            print('[INFO] File downloaded! ->', wind_filename)
            break
        except:
            continue

    return wind_filename


def load_data(filename, date, time_window):
    """Loads filtered data."""

    print("[INFO] Loading file ->", filename)
    wind_cdf_data = cdflib.cdf_to_xarray(filename,
                                         to_datetime=True,
                                         fillval_to_nan=True)

    wind_data = wind_cdf_data['BGSE'].to_pandas()
    wind_data.columns = ['x', 'y', 'z']
    wind_data['BF1'] = wind_cdf_data['BF1'].to_pandas()
    wind_data['norm'] = np.linalg.norm(wind_data[['x', 'y', 'z']].values,
                                       axis=1)

    start_t, end_t = time_window
    start_date = f'{date} {start_t}'
    end_date = f'{date} {end_t}'

    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

    wind_mask = (wind_data.index > start_date) & (wind_data.index <= end_date)
    filtered_data = wind_data.loc[wind_mask]

    return wind_data, filtered_data
