import matplotlib.pyplot as plt
from datetime import datetime as dt


class Chart:

    def __init__(self, data):
        self.data = data


    def draw_pie(self, data):
        labels = data[0]
        values = data[1]
        #totals = data[2] #asset class totals

        now = dt.now()
        time = now.strftime("%d-%m-%Y-%H%M")

        # Plot
        plt.pie(values, labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        path = "../data/plot"+time+".png"
        plt.savefig(path)