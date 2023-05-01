import pickle as pkl

with open("results/2023-04-20 18:25:15.376824.pkl", "rb") as f:
    data = pkl.load(f)

print(data)
