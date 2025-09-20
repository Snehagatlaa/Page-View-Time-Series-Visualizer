# main.py
import matplotlib.pyplot as plt
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Generate and show/save plots
if __name__ == "__main__":
    # Line plot
    fig1 = draw_line_plot()
    fig1.show()

    # Bar plot
    fig2 = draw_bar_plot()
    fig2.show()

    # Box plots
    fig3 = draw_box_plot()
    fig3.show()
