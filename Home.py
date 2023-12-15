import streamlit as st

st.header("Burinchai Sukon")

import numpy as np
import matplotlib.pyplot as plt
data = [[30, 25, 50, 20],
[40, 23, 51, 17],
[35, 22, 45, 19]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'teal', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'pink', width = 0.25)
ax.bar(X + 0.50, data[2], color = 'orange', width = 0.25)
ax.legend(labels=['Datascience', 'ComputerEd','InforamtonTech'])