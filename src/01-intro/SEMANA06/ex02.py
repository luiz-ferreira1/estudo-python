import pandas as pd

df = pd.read_csv('src/01-intro/SEMANA06/classification_results_trial_0001.csv')

erros = df[df['real_class'] != df['predicted_class']]

print(erros[['image_path', 'real_class', 'predicted_class']])