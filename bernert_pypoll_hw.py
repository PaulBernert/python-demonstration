import pandas as pd

df = pd.read_csv("PyPoll/Resources/election_data.csv")

tot_votes = df.Candidate.count()
winner = df.groupby('Candidate').count().County.idxmax()

x = df.Candidate.unique()
z = df["Candidate"].value_counts()
y = ((z / tot_votes) * 100).round(2)

with open("PyPoll/bernert_pypoll_output.csv",'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {tot_votes}\n")
    f.write("-------------------------\n")
    for i in range(4):
        f.write(f"{x[i]}: {y[i]}% ({z[i]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")