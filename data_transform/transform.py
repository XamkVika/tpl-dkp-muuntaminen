import pandas as pd


# -----------------------------------------------------------
# Student tasks (skeletons) — opiskelija toteuttaa nämä
# -----------------------------------------------------------


def clean_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tehtävä: Siivoa tekstisarakkeet kuten 'name' ja 'capital'.

    Ohjeet:
    - Käytä pandasin `.str`-metodeja
    - Poista ympäröivät välilyönnit
    - Muuta esimerkiksi title-caseen
    - Poista tarvittaessa numerot ja erikoismerkit

    Palauta siivottu DataFrame.
    """
    # TODO: opiskelijan toteutus
    return df


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tehtävä: Käsittele puuttuvat arvot.

    Ohjeet:
    - Korvaa "N/A" ja vastaavat merkeillä `pd.NA`
    - Tulosta kuinka monta puuttuvaa arvoa sarakkeissa on
    - Poista rivit, joilta puuttuu esim. 'capital'

    Palauta DataFrame, jossa puuttuvat arvot käsitelty.
    """
    # TODO: opiskelijan toteutus
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tehtävä: Poista duplikaatit.

    Ohjeet:
    - Poista päällekkäiset rivit perustuen esim. 'name' (case-insensitive)
    - Palauta puhdistettu DataFrame
    """
    # TODO: opiskelijan toteutus
    return df


def fix_types_and_sort(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tehtävä: Korjaa sarakkeiden tyypit ja järjestä.

    Ohjeet:
    - Kokeile muuntaa numeromuotoiset sarakkeet numeerisiksi
    - Järjestä DataFrame nimen mukaan
    """
    # TODO: opiskelijan toteutus
    return df


def clean_dataframe(df: pd.DataFrame, save_path: str | None = None) -> pd.DataFrame:
    """Suorittaa kaikki siivousvaiheet peräkkäin (kutsuu yllä olevia funktioita)."""
    df = df.copy()
    df = clean_strings(df)
    df = handle_missing(df)
    df = remove_duplicates(df)
    df = fix_types_and_sort(df)

    if save_path:
        df.to_csv(save_path, index=False)
    return df


__all__ = [
    "clean_strings",
    "handle_missing",
    "remove_duplicates",
    "fix_types_and_sort",
    "clean_dataframe",
]
