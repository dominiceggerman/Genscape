# By Dominic Eggerman
import pandas

if __name__ == '__main__':
    # Read the csv file into a variable
    df = pandas.read_csv("Wagoner East (2).csv")
    # print(df)

    # # Accessing a row
    # print(df["Effective Date"].values)

    # # Print date and scheduled cap
    # for x in df:
    #     print(x)

    # # Loop done right
    # for date, flow in zip(df["Effective Date"].values, df["Scheduled (BZ)"].values):
    #     print(date + " : " + str(flow))

    # # Change up columns
    # mmcf = df.loc[:, "Scheduled (BZ)"] / 1030  # Applying scalar to column, makes a series (list)
    # mmcf = round(mmcf, 2)  # Round to 2 DP
    # df["Scheduled (MMcf)"] = mmcf  # Adding column to df.  There are different ways to do this
    # df = df.drop(columns=["Design (BZ)", "Available (BZ)"])  # Drop the design cap column
    # df = df[["Effective Date", "Scheduled (BZ)", "Scheduled (MMcf)", "Operational (BZ)"]]  # Rearrange the columns
    # print(df)
    
    # # Ouput with different column headers and no index
    # df.to_csv("output_data.csv", header=["Date", "Sched (BZ)", "Sched (MMcf)", "Opcap (BZ)"], index=False)