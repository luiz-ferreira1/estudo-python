import pandas as pd

df = pd.read_csv('src/01-intro/SEMANA06/classification_results_trial_0001.csv')

malign = df[df['real_class'] == 'malign']

resultado = malign.nlargest(5, 'prob_benign')

print(resultado[['image_path', 'real_class', 'predicted_class', 'prob_benign']])