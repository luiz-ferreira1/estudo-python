import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('src/01-intro/SEMANA06/metrics.csv')

epocas = range(1, len(df) + 1)

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
fig.suptitle('Métricas de Treinamento por Época', fontsize=14)

# 1. Gráfico de barras: train_loss por época
axes[0, 0].bar(epocas, df['train_loss'], color='steelblue')
axes[0, 0].set_title('Train Loss por Época')
axes[0, 0].set_xlabel('Época')
axes[0, 0].set_ylabel('Loss')

# 2. Gráfico de barras: val_loss por época
axes[0, 1].bar(epocas, df['val_loss'], color='tomato')
axes[0, 1].set_title('Val Loss por Época')
axes[0, 1].set_xlabel('Época')
axes[0, 1].set_ylabel('Loss')

# 3. Histograma de train_acc
axes[0, 2].hist(df['train_acc'], bins=15, color='steelblue')
axes[0, 2].set_title('Histograma de train_acc')
axes[0, 2].set_xlabel('Acurácia')
axes[0, 2].set_ylabel('Frequência')

# 4. Histograma de val_acc
axes[1, 0].hist(df['val_acc'], bins=15, color='tomato')
axes[1, 0].set_title('Histograma de val_acc')
axes[1, 0].set_xlabel('Acurácia')
axes[1, 0].set_ylabel('Frequência')

# 5. Scatter: train_acc vs val_acc
axes[1, 1].scatter(df['train_acc'], df['val_acc'], color='purple', alpha=0.6)
axes[1, 1].set_title('Scatter: train_acc vs val_acc')
axes[1, 1].set_xlabel('train_acc')
axes[1, 1].set_ylabel('val_acc')

# 6. train_loss vs val_loss ao longo das épocas
axes[1, 2].plot(epocas, df['train_loss'], label='train_loss', color='steelblue')
axes[1, 2].plot(epocas, df['val_loss'],   label='val_loss',   color='tomato')
axes[1, 2].set_title('Train Loss vs Val Loss')
axes[1, 2].set_xlabel('Época')
axes[1, 2].set_ylabel('Loss')
axes[1, 2].legend()

plt.tight_layout()
plt.savefig('graficos_metrics.png', dpi=150)
print('Salvo em graficos_metrics.png')