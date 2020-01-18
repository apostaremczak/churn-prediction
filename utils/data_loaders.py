import numpy as np
import pandas as pd


def load_train_churn(file_path: str) -> pd.DataFrame:
    """
    Reads training data.
    Columns:
    - user_id (string)
    - is_churn (int, 0 or 1)
    """
    churn = pd.read_csv(file_path)
    churn.rename({"msno": "user_id"}, axis=1, inplace=True)
    churn["is_churn"] = churn.is_churn.astype(np.uint8)
    return churn


def load_member_transactions(file_path: str) -> pd.DataFrame:
    """
    Reads processed member & transaction details.
    """
    df = pd.read_csv(file_path)
    # Change column types for decreased memory use

    # Int-8 columns
    int_8_cols = [
                     "payment_method_id",
                     "gender_female",
                     "gender_male",
                     "gender_unknown",
                     "is_discount",
                     "is_auto_renew",
                     "is_cancel",
                     "registered_via_13",
                     "registered_via_14",
                     "registered_via_255",
                     "city_1"
                 ] + [
                     f"city_{i}" for i in range(3, 23)
                 ] + [
                     f"registered_via_{i}" for i in range(1, 12)
                 ] + [
                     f"registered_via_{i}" for i in range(16, 20)
                 ]

    for col in int_8_cols:
        df[col] = df[col].astype(np.uint8)

    # Int-16 columns
    int_16_cols = [
        "purchased_membership_length_days",
        "price_ntd",
        "amount_paid_ntd",
        "time_since_registration",
        "discount"
    ]

    for col in int_16_cols:
        df[col] = df[col].astype(np.uint16)

    return df
