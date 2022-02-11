

import pandas as pd

address = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'

# Assign the data to a variable called euro12
euro12 = pd.read_csv(address)

# Select the goal column
euro12.Goals

# How many teams participated in Euro2012?
euro12.Team.nunique()

# Number of columns
euro12.shape[1]

# View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# Sort the teams by red cards, then yellow cards
discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)

# Mean yellow cards per team
discipline['Yellow Cards'].mean()

# Teams that scored more than 6 goals
euro12[euro12.Goals > 6]

# Teams that starts with G
euro12[euro12.Team.str.startswith('G')]

# First 7 columns
euro12.head(7)

# All the columns except the last 3
euro12[euro12.columns[:-3]]

# Shooting accuracy from England, Italy and Russia
teams_filter = ['England', 'Italy', 'Russia']
euro12[euro12.Team.isin(teams_filter)][['Team', 'Shooting Accuracy']]

