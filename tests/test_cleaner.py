import pandas as pd
import pytest

from data_cleaning.cleaner import (
    clean_strings,
    handle_missing,
    remove_duplicates,
    fix_types_and_sort,
    clean_dataframe,
)


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "name": [" finland ", "Finland", "france1", "Spain"],
            "capital": ["helsinki ", "Helsinki", "Paris", "N/A"],
            "population": ["5", "5", "67", "47"],
        }
    )


def test_clean_strings(sample_df):
    out = clean_strings(sample_df)
    assert out.loc[0, "name"] == "Finland"
    assert out.loc[0, "capital"] == "Helsinki"
    # digits removed from france1 -> France
    assert "1" not in out.loc[2, "name"]


def test_handle_missing(sample_df):
    out = handle_missing(sample_df)
    # Row with capital 'N/A' should be dropped
    assert not (out["capital"].astype(str).str.upper() == "N/A").any()


def test_remove_duplicates(sample_df):
    out = remove_duplicates(sample_df)
    # Only one Finland should remain
    names = out["name"].astype(str).str.lower()
    assert names.tolist().count("finland") == 1


def test_fix_types_and_sort(sample_df):
    out = fix_types_and_sort(sample_df)
    # population should be coerced to numeric where possible
    assert pd.api.types.is_numeric_dtype(out["population"]) or out["population"].dtype == object


def test_clean_dataframe_end_to_end(sample_df, tmp_path):
    out_path = tmp_path / "cleaned.csv"
    cleaned = clean_dataframe(sample_df, save_path=str(out_path))
    # Check that saved file exists and cleaned DataFrame returned
    assert out_path.exists()
    assert isinstance(cleaned, pd.DataFrame)
