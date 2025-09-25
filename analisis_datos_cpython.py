# Carguemos los datos
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

cpython = pd.read_csv("https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/refs/heads/master/cpython_commit_history_pre.csv")

# Crear columnas a partir de la columna date
cpython["date"] = pd.to_datetime(cpython["date"], utc = True)

# Construyamos la columna year
cpython["year"] = cpython["date"].dt.year
cpython["month"] = cpython["date"].dt.to_period("M")

# Contemos la cantidad de commits por año

plt.figure(figsize=(16,9))
commits_per_year = cpython.groupby("year").size()
commits_per_year.plot(kind = "line", marker="o")
plt.title("Evolucion de commits por año : CPYTHON")
plt.xlabel("Año")
plt.ylabel("Numero de commits")
plt.grid(True)
# Guardemos a disco duro la imagen generada 
plt.savefig("cpython_num_commits_year.png", dpi = 300)
plt.show()

# Top10 de contribuyentes
cpython["author"].value_counts().head(10).plot(kind = "barh", color = "skyblue")
plt.gca().invert_yaxis()
plt.savefig("cpython_top10_developers.png", dpi = 300)
plt.show()


# Esta linea es agregada en un notebook de kaggle
