import pandas as pd

df = pd.read_csv('src/01-intro/SEMANA06/classification_results_trial_0001.csv')

TP = len(df[(df['real_class'] == 'malign') & (df['predicted_class'] == 'malign')])
TN = len(df[(df['real_class'] == 'benign') & (df['predicted_class'] == 'benign')])
FP = len(df[(df['real_class'] == 'benign') & (df['predicted_class'] == 'malign')])
FN = len(df[(df['real_class'] == 'malign') & (df['predicted_class'] == 'benign')])

print(f'TP: {TP}')
print(f'TN: {TN}')
print(f'FP: {FP}')
print(f'FN: {FN}')