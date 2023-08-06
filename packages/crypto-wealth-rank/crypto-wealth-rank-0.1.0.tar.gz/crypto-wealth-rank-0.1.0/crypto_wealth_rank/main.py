def rank_wealth(balance: float | int | None) -> str | None:
    if balance is None:
        return None

    wealth_ranks = {
        1: 'Shrimp',
        10: 'Crab',
        50: 'Octopus',
        100: 'Fish',
        500: 'Dolphin',
        1000: 'Shark',
        5000: 'Whale',
    }

    try:
        balance = float(balance)
    except ValueError as error:
        raise ValueError('balance must be an integer or a float') from error

    return next(
        (
            rank
            for rank_balance, rank in wealth_ranks.items()
            if balance <= rank_balance
        ),
        'HumpBack Whale',
    )
