import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo
df = pd.read_csv("lecturas_oscilloscope.csv")

# Filtrar filas específicas df = df.iloc[381472:381555].copy()
df = df.iloc[381472:381555].copy()

# Combinar fecha y hora
df['Datetime'] = pd.to_datetime(df['Fecha'].astype(str) + ' ' + df['Hora'].astype(str), format='mixed')

# Calcular tiempo transcurrido en segundos
df['TimeSeconds'] = (df['Datetime'] - df['Datetime'].iloc[0]).dt.total_seconds()
df = df[df['TimeSeconds'] > 0]  # Evita log(0)

# Crear la gráfica
plt.figure(figsize=(14, 6))
plt.plot(df['TimeSeconds'], df['Voltaje (mV)'], linewidth=0.5)
plt.xlabel('Tiempo transcurrido (segundos)')
plt.ylabel('Voltaje (mV)')
plt.title('Voltaje vs. Tiempo (filas 353460 a 729319)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Guardar en archivo PNG
plt.savefig("grafica_voltage_log.png", dpi=300)
print("Gráfica guardada como 'grafica_voltage_log.png'")