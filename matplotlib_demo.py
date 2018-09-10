# By Dominic Eggerman
# https://matplotlib.org/users/pyplot_tutorial.html - Starting tutorial
# https://matplotlib.org/tutorials/introductory/sample_plots.html - Types of plots
import pandas
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Plot the data we created in pandas

    # Load data
    df = pandas.read_csv("output_data.csv")
    # print(df)

    # # Basic plot
    # plt.plot(df["Date"].values, df["Sched (MMcf)"].values)
    # plt.plot(df["Date"].values, df["Opcap (BZ)"].values / 1030)
    # plt.ylabel("MMcf/d")
    # plt.title("Wagoner East flows")
    # plt.legend()
    # plt.show()  # Show plot

    # # This looks messy - cleanup
    # plt.plot(df["Date"].values, df["Sched (MMcf)"].values, label="Scheduled", color="green", linestyle="dashed")
    # plt.plot(df["Date"].values, df["Opcap (BZ)"].values / 1030, label="Operational", color="blue", linestyle="solid")
    # plt.ylabel("MMcf/d")
    # plt.title("Wagoner East flows")
    # plt.legend()

    # plt.xticks(df["Date"].values[::2], rotation=90)
    # plt.legend().draggable()
    # plt.tight_layout()

    # plt.show()

    # See tutorials for more plot types