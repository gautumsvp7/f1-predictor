import pandas as pd

def preprocess_input_data(df):
    # Fill NaNs
    cols_to_fill_1 = ['Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3Time']
    df[cols_to_fill_1] = df[cols_to_fill_1].fillna(0)

    df['IsPersonalBest'] = df['IsPersonalBest'].replace({True: 1, False: 0})

    cols_to_fill_2 = ['SpeedI1','SpeedI2','SpeedFL','SpeedST']
    df[cols_to_fill_2] = df[cols_to_fill_2].fillna(0)

    df.dropna(subset=['LapTime'], inplace=True)
    df.dropna(subset=['TyreLife'], inplace=True)

    df[['Sector2Time', 'Sector3SessionTime']] = df[['Sector2Time', 'Sector3SessionTime']].fillna(0)

    df['Deleted'] = df['Deleted'].replace({True: 1, False: 0})
    df['FreshTyre'] = df['FreshTyre'].replace({True: 1, False: 0})

    # Compound mapping
    df['Compound'] = df['Compound'].replace({
        'SUPERSOFT': 1,
        'SOFT': 2,
        'ULTRASOFT': 3,
        'MEDIUM': 4,
        'HARD': 5
    })
    team_mapping = {
    'Toro Rosso': 1,
    'Force India': 2,
    'McLaren': 3,
    'Sauber': 4,
    'Williams': 5,
    'Haas F1 Team': 6,
    'Renault': 7,
    'Red Bull Racing': 8,
    'Mercedes': 9,
    'Ferrari': 10,
    'Alfa Romeo Racing': 11,
    'Racing Point': 12,
    'AlphaTauri': 13,
    'Alpine': 14,
    'Aston Martin': 15,
    'Alfa Romeo': 16,
    'RB': 17,
    'Kick Sauber': 18,
    'Racing Bulls': 19
    }

    df['Team'] = df['Team'].replace(team_mapping)
    time_columns = ['LapTime', 'Sector1Time', 'Sector2Time', 'Sector3Time','Sector1SessionTime','Sector2SessionTime','Sector3SessionTime','LapStartTime' ]

    for col in time_columns:
        df[col] = pd.to_timedelta(df[col])
        df[col + '_s'] = df[col].dt.total_seconds()


        df['PitInTime'] = pd.to_timedelta(df['PitInTime'], errors='coerce')


    df['PitInTime_s'] = df['PitInTime'].dt.total_seconds()
    df['PitInTime_s'] = df['PitInTime_s'].fillna(0)
    df = df.drop('PitInTime', axis=1)
    df['PitOutTime'] = pd.to_timedelta(df['PitOutTime'], errors='coerce')
    df['PitOutTime_s'] = df['PitOutTime'].dt.total_seconds()

    df['PitOutTime_s'] = df['PitOutTime_s'].fillna(0)
    df = df.drop('PitOutTime', axis=1)

    df['LapStartTime'] = pd.to_timedelta(df['LapStartTime'], errors='coerce')

    df['LapStartTime_s'] = df['LapStartTime'].dt.total_seconds()

    df['LapStartTime_s'] = df['LapStartTime_s'].fillna(0)

    df = df.drop('LapStartTime', axis=1)

    df['LapStartDate'] = pd.to_timedelta(df['LapStartDate'], errors='coerce')

    df['LapStartDate_s'] = df['LapStartDate'].dt.total_seconds()

    df['LapStartDate_s'] = df['LapStartDate_s'].fillna(0)

    df = df.drop('LapStartDate', axis=1)

    return df
