from src.data.load_data import load_data

fake_df, true_df = load_data()

print()
print("Fake Shape :", fake_df.shape)
print("True Shape :", true_df.shape)