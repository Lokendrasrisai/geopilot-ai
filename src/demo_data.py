import pandas as pd
import numpy as np

def get_demo_dataset(vertical: str) -> pd.DataFrame:
    rng = np.random.default_rng(42)

    if vertical == "GIS / Local Government":
        df = pd.DataFrame({
            "asset_id": [f"A{i:03d}" for i in range(1, 61)],
            "latitude": rng.normal(39.80, 0.02, 60),
            "longitude": rng.normal(-89.65, 0.03, 60),
            "status": rng.choice(["active", "inactive", "unknown", "tbd"], 60, p=[0.55, 0.15, 0.18, 0.12]),
            "inspection_date": rng.choice(["2025-01-12", "2024-11-03", None, "2023-07-01"], 60),
            "asset_type": rng.choice(["hydrant", "road_segment", "sign", "signal"], 60),
            "priority": rng.choice(["low", "medium", "high", None], 60),
            "jurisdiction": rng.choice(["north", "south", "west", None], 60)
        })
        df.loc[[5, 11], "latitude"] = [99.1, -130.0]
        df.loc[[8, 19], "longitude"] = [250.2, -500.5]
        df = pd.concat([df, df.iloc[[2]]], ignore_index=True)
        return df

    if vertical == "Public Safety":
        df = pd.DataFrame({
            "address_id": [f"ADDR{i:03d}" for i in range(1, 61)],
            "latitude": rng.normal(39.80, 0.02, 60),
            "longitude": rng.normal(-89.65, 0.03, 60),
            "status": rng.choice(["verified", "pending", "invalid", "missing"], 60, p=[0.48, 0.24, 0.18, 0.10]),
            "zone": rng.choice(["Z1", "Z2", "Z3", None], 60),
            "response_area": rng.choice(["R1", "R2", None], 60),
            "street_name": rng.choice(["Main", "Oak", "Pine", None], 60),
            "updated_at": rng.choice(["2025-02-01", "2024-12-19", None], 60)
        })
        df.loc[[4, 9], "latitude"] = [91.0, -95.4]
        return df

    if vertical == "Utilities":
        df = pd.DataFrame({
            "asset_id": [f"U{i:03d}" for i in range(1, 61)],
            "status": rng.choice(["active", "inactive", "unknown", "null"], 60, p=[0.52, 0.18, 0.20, 0.10]),
            "asset_type": rng.choice(["transformer", "line", "pole", "meter"], 60),
            "inspection_date": rng.choice(["2025-03-10", None, "2024-08-17"], 60),
            "installation_year": rng.choice([1998, 2005, 2011, None, 2020], 60),
            "condition_score": rng.choice([0.2, 0.5, 0.9, None, 1.4, -0.2], 60),
            "feeder": rng.choice(["F1", "F2", None], 60)
        })
        df = pd.concat([df, df.iloc[[7]]], ignore_index=True)
        return df

    if vertical == "Campus / Indoors":
        df = pd.DataFrame({
            "space_id": [f"S{i:03d}" for i in range(1, 61)],
            "building": rng.choice(["Science", "Library", "Union", None], 60),
            "floor": rng.choice([1, 2, 3, 4, None, -1], 60),
            "status": rng.choice(["active", "temp", "unknown", "inactive"], 60, p=[0.5, 0.14, 0.18, 0.18]),
            "category": rng.choice(["lab", "office", "classroom", None], 60),
            "capacity": rng.choice([10, 20, 40, None, 500], 60),
            "updated_at": rng.choice(["2025-01-01", None, "2024-05-15"], 60),
            "accessible": rng.choice(["yes", "no", None], 60)
        })
        return df

    df = pd.DataFrame({
        "record_id": [f"R{i:03d}" for i in range(1, 61)],
        "status": rng.choice(["active", "unknown", "tbd", "na"], 60, p=[0.54, 0.16, 0.18, 0.12]),
        "created_at": rng.choice(["2025-01-01", "2024-09-12", None], 60),
        "updated_at": rng.choice(["2025-03-01", None, "2024-10-10"], 60),
        "owner": rng.choice(["ops", "analytics", None, "field"], 60),
        "category": rng.choice(["A", "B", "C", None], 60),
        "value_1": rng.normal(100, 25, 60),
        "value_2": rng.normal(50, 10, 60)
    })
    df.loc[[3, 14], "value_1"] = [999, -400]
    return df
