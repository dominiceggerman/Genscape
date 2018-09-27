# By Dominic Eggerman
import pandas

if __name__ == '__main__':
    # Read the csv file into a variable
    df = pandas.read_csv("Wagoner East (2).csv")
    # print(df)

    # # Accessing a row
    # print(df.loc[[0]])
    # # Accessing a column
    # print(df["Effective Date"].values)

    # # Print date and scheduled cap (wrong)
    # for x in df:
    #     print(x)

    # One way to do this loop
    # for date, flow in zip(df["Effective Date"].values, df["Scheduled (BZ)"].values):
    #     print(date + " : " + str(flow))

    # # Change up columns
    # mmcf = df.loc[:, "Scheduled (BZ)"] / 1030  # Applying scalar to column, makes a series (list)
    # mmcf = round(mmcf, 2)  # Round to 2 DP
    # df["Scheduled (MMcf)"] = mmcf  # Adding column to df.  There are different ways to do this
    # df = df.drop(columns=["Design (BZ)", "Available (BZ)", "Operational (BZ)"])  # Drop the columns we dont want
    # df = df[["Effective Date", "Scheduled (BZ)", "Scheduled (MMcf)", "Operational (BZ)"]]  # Rearrange the columns
    # df = df.iloc[::-1]  # Reverse rows of df
    # print(df)
    
    # # Ouput with different column headers and no index
    # df.to_csv("output_data.csv", header=["Date", "Sched (BZ)", "Sched (MMcf)"], index=False)