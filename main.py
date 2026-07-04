from src.data.load_data import load_data
from src.data.validate_data import validate_dataframe
from src.data.preprocess import create_master_dataset

fake_df, true_df = load_data()

validate_dataframe(fake_df, "Fake")
validate_dataframe(true_df, "True")

news_df = create_master_dataset(
    fake_df,
    true_df
)

print()
print(news_df.head())

print()

print(news_df.shape)