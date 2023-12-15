import streamlit as st

st.header("Burinchai Sukon")

import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Python", "R", "Java", "Php"]
myexplode = [0, 0, 0, 0.15]
plt.pie(y, labels = mylabels, startangle = 90,explode = myexplode,shadow=True)
plt.title("Popular Program in Datascince")
plt.show()