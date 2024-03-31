import numpy as np


def calculate_score(han: int, fu: int, is_dealer=False, kiriage=False, honba=0) -> dict:
    if fu > 20 and fu < 25:
        fu = 25
    elif fu % 10 != 0:
        fu = fu + (10 - fu % 10)

    special_name = None
    base_score = fu * 2 ** (2 + han)
    # base_score = fu * 4 * (2 ** han) can also be used, but the former is more simplified
    if (kiriage and base_score == 1920) or base_score > 2000 or han == 5:
        # Mangan and Kiriage Mangan (4 han/30 fu and 3 han/60 fu)
        base_score = 2000
        special_name = 'Mangan'
    if han in (6, 7):  # Haneman
        base_score = 3000
        special_name = 'Haneman'
    elif han in (8, 9, 10):  # Baiman
        base_score = 4000
        special_name = 'Baiman'
    elif han in (11, 12):  # Sanbaiman
        base_score = 6000
        special_name = 'Sanbaiman'
    elif han >= 13:  # Yakuman
        base_score = 8000
        special_name = 'Kazoe Yakuman'
    score_dict = {
        'han': han,
        'fu': fu,
        'honba': honba,
        'dealer': is_dealer,
        'kiriage': kiriage,
        'special_name': special_name if special_name else None,
    }
    if is_dealer:
        ron = np.ceil(base_score * 6 / 100) * 100 + honba * 300
        score_dict['ron'] = f"{int(ron)}"
        tsumo = np.ceil(base_score * 2 / 100) * 100 + honba * 100
        score_dict['tsumo'] = f"{int(tsumo)} all"
    else:
        ron = np.ceil(base_score * 4 / 100) * 100 + honba * 300
        tsumo_oya = np.ceil(base_score * 2 / 100) * 100 + honba * 100
        tsumo_ko = np.ceil(base_score / 100) * 100 + honba * 100
        score_dict['ron'] = f"{int(ron)}"
        score_dict['tsumo'] = f"{int(tsumo_oya)}/{int(tsumo_ko)}"
    return score_dict
