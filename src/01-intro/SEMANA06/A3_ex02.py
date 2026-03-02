import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('src/01-intro/SEMANA06/metrics.csv')

epocas = range(1, len(df) + 1)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico 1: model accuracy
axes[0].plot(epocas, df['train_acc'], label='train', color='steelblue')
axes[0].plot(epocas, df['val_acc'],   label='valid',  color='orange')
axes[0].set_title('model accuracy')
axes[0].set_xlabel('epoch')
axes[0].set_ylabel('accuracy')
axes[0].legend()

# Gráfico 2: model loss
axes[1].plot(epocas, df['train_loss'], label='train', color='steelblue')
axes[1].plot(epocas, df['val_loss'],   label='valid',  color='orange')
axes[1].set_title('model loss')
axes[1].set_xlabel('epoch')
axes[1].set_ylabel('loss')
axes[1].legend()

plt.tight_layout()
plt.savefig('graficos_curvas.png', dpi=150)
print('Salvo em graficos_curvas.png')