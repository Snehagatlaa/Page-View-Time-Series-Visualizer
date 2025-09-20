# test_module.py
import unittest
import matplotlib as mpl

mpl.use('Agg')  # Use non-interactive backend for testing

import time_series_visualizer as tsv


class TestTimeSeriesVisualizer(unittest.TestCase):

    def setUp(self):
        self.fig_line = tsv.draw_line_plot()
        self.fig_bar = tsv.draw_bar_plot()
        self.fig_box = tsv.draw_box_plot()

    def test_draw_line_plot(self):
        self.assertEqual(self.fig_line.__class__.__name__, 'Figure')
        self.assertEqual(len(self.fig_line.axes[0].lines), 1)
        self.assertEqual(self.fig_line.axes[0].get_title(),
                         "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
        self.assertEqual(self.fig_line.axes[0].get_xlabel(), "Date")
        self.assertEqual(self.fig_line.axes[0].get_ylabel(), "Page Views")

    def test_draw_bar_plot(self):
        self.assertEqual(self.fig_bar.__class__.__name__, 'Figure')
        self.assertEqual(len(self.fig_bar.axes[0].patches), 48)
        self.assertEqual(self.fig_bar.axes[0].get_xlabel(), "Years")
        self.assertEqual(self.fig_bar.axes[0].get_ylabel(), "Average Page Views")
        self.assertEqual(self.fig_bar.axes[0].get_legend().get_title().get_text(), "Months")

    def test_draw_box_plot(self):
        self.assertEqual(self.fig_box.__class__.__name__, 'Figure')
        self.assertEqual(len(self.fig_box.axes), 2)
        self.assertEqual(self.fig_box.axes[0].get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(self.fig_box.axes[1].get_title(), "Month-wise Box Plot (Seasonality)")
        self.assertEqual(self.fig_box.axes[0].get_xlabel(), "Year")
        self.assertEqual(self.fig_box.axes[0].get_ylabel(), "Page Views")
        self.assertEqual(self.fig_box.axes[1].get_xlabel(), "Month")
        self.assertEqual(self.fig_box.axes[1].get_ylabel(), "Page Views")


if __name__ == "__main__":
    unittest.main()
