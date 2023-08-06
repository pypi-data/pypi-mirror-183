# Crypto Wealth Rank

[![Downloads](https://static.pepy.tech/personalized-badge/crypto-wealth-rank?period=total&units=none&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/crypto-wealth-rank)

A simple python package to get crypto wealth rank.

ranks are as follows:

`Shrimp: less than 1 BTC` <br />
`Crab: 1 to 10 BTC` <br />
`Octopus: 10 to 50 BTC` <br />
`Fish: 50 to 100 BTC` <br />
`Dolphin: 100 to 500 BTC` <br />
`Shark: 500 to 1000 BTC` <br />
`Whale: >1000 BTC` <br />
`Humpback: >5000 BTC` <br />

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Install the package using pip:

```sh
pip install crypto-wealth-rank
```

## Usage

```python
from crypto_wealth_rank import rank_wealth

eth_balance = 100
rank = rank_wealth(eth_balance)
print(rank)  # Fish
```

## Support

Please [open an issue](https://github.com/apinanyogaratnam/crypto-wealth-rank/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/apinanyogaratnam/crypto-wealth-rank/compare/).
