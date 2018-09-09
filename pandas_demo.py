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

    