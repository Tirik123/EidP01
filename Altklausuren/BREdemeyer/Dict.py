from typing import Any


def sr_info(data: dict[int, dict[str, set[str]]]) -> dict[str, dict[set[int] | set[str]]]:
    new_dict = {}
    #new_inner_dict = {}
    for databank, inner_dict in data.items():   # databank = 130001; inner_dict = {"league: l1", "sr": {"SR A", SR C}}
        for keys, values in inner_dict.items(): # keys = "league", "sr"; values = "l1", {"SR A", " SR C"}
            if keys == "sr":                    # keys = "sr"
                for sr in values:               # iterate over {"SR A", "SR C"}
                    new_dict[sr] = dict()       # Keys() of new_dict are "SR A", "SR C"; Values() are empty dict()
            if keys == "league":
                for keyz, valuez in new_dict.items():
                    valuez["leagues"] = values
    print(new_dict)






if __name__ == '__main__':
    data: dict[int, dict[str, Any]] = {
    130001: {
        "league": "l1",
        "sr": {"SR A", "SR C"},
    },
    130002: {
        "league": "l2",
        "sr": {"SR B"},
    },
    130003: {
        "league": "l1",
        "sr": {"SR C", "SR D"},
    },
    130004: {
        "league": "l2",
        "sr": {"SR A"},
    },
}
    
    print(sr_info(data))