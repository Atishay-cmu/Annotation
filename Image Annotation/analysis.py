import pickle as pkl

with open("results/2023-05-14 20:06:29.633776.pkl", "rb") as f:
    data = pkl.load(f)

print(data)

# prolific ID, fouunder image, ...
# 2 tables - one images and one for the annotators
