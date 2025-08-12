"""
report.py input.csv output.pdf
Generates a simple PDF with summary statistics and a histogram.
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def make_report(infile, outfile):
    df = pd.read_csv(infile)
    with PdfPages(outfile) as pdf:
        desc = df.describe()
        fig, ax = plt.subplots(figsize=(8,2))
        ax.axis('off')
        ax.table(cellText=desc.round(2).values, colLabels=desc.columns, rowLabels=desc.index, loc='center')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()

        # histogram of first numeric column
        nums = df.select_dtypes(include=['number']).columns
        if len(nums):
            fig = df[nums[0]].plot(kind='hist').get_figure()
            fig.suptitle(f'Histogram: {nums[0]}')
            pdf.savefig(fig)
            plt.close()
        else:
            print("No numeric columns to plot")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python report.py input.csv output.pdf")
    else:
        make_report(sys.argv[1], sys.argv[2])
