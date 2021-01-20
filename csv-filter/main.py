import pandas
import datetime
import re

# Target file name (located in the ./input folder)
target_file = 'data_trump admin'

# Title of the column in which to filter results ('description' or 'title')
col_title = 'title'

# Look for crisis related results?
crisis_mode = True

# Keywords by which to filter
keywords = [
  'oversight',
  'review',
  'report',
  'budget request',
  'control',
  'impact',
  'information',
  'investigation',
  'request',
  'explanation',
  'president',
  'administration',
  'contract',
  'consultation',
  'examination',
]

# Additional keywords
crisis_keywords = [
  'coronavirus',
  'covid',
  'pandemic'
  'protest',
  'unrest',
  'george floyd',
  'brutality',
  'police',
  'crisis'
]

# crisis_keywords = [
#   'terror',
#   'attack',
#   'qaeda',
#   'qaida',
#   'taliban',
#   'iraq',
#   'afghanistan',
# ]

# ======================
# No need to edit below.
# ======================

df = pandas.read_csv('input/' + target_file + '.csv')


keywordRegex = '|'.join(keywords)
crisisRegex = '|'.join(crisis_keywords)


print('There are ' + str(len(df)) + ' rows in the dataset before filtering by one of the keywords:')
print(keywordRegex)
if crisis_mode:
  print('AND')
  print(crisisRegex)
print()

t1 = datetime.datetime.now()
new_df = df[df[col_title].str.contains(keywordRegex, flags=re.IGNORECASE, regex=True)]

if crisis_mode:
  new_df = new_df[new_df[col_title].str.contains(crisisRegex, flags=re.IGNORECASE, regex=True)]

if (crisis_mode):
  target_file += '_filtered-crisis'
else:
  target_file += '_filtered'

new_df.to_csv('output/' + target_file + '.csv')
t2 = datetime.datetime.now()
deltaTime = round((t2 - t1).total_seconds(), 2)

print('Filter operation took ' + str(deltaTime) + ' seconds to complete.')

print()

print('There are ' + str(len(new_df)) + ' rows in the dataset after filtering by one of the keywords.')