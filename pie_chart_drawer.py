import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from categoriser import summed_categories

# take the summed categories df from categoriser.py
# draw a pie chart using categories as wedges and values as the size of each wedge


def draw_pie_chart(categories, values):
    y = np.array(values)
    mylabels = categories
    plt.pie(y, labels=mylabels)
    plt.title("Spending by Category")
    plt.show()

draw_pie_chart(summed_categories["Category"], summed_categories["Money Out"])