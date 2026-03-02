import pandas as pd

df = pd.read_csv('src/01-intro/SEMANA06/classification_results_trial_0001.csv')

TP = len(df[(df['real_class'] == 'malign') & (df['predicted_class'] == 'malign')])
TN = len(df[(df['real_class'] == 'benign') & (df['predicted_class'] == 'benign')])
FP = len(df[(df['real_class'] == 'benign') & (df['predicted_class'] == 'malign')])
FN = len(df[(df['real_class'] == 'malign') & (df['predicted_class'] == 'benign')])

acuracia      = (TP + TN) / (TP + TN + FP + FN)
precisao      = TP / (TP + FP)
recall        = TP / (TP + FN)
especificidade = TN / (TN + FP)

print(f'Acurácia:       {acuracia:.2f}')
print(f'Precisão:       {precisao:.2f}')
print(f'Recall:         {recall:.2f}')
print(f'Especificidade: {especificidade:.2f}')