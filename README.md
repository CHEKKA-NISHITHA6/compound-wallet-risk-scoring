# Compound V2 Wallet Risk Scoring

This project assigns credit risk scores (0–1000) to Ethereum wallets based on their simulated Compound V2 protocol activity.

## Features Used

- `total_borrows`
- `total_repays`
- `borrow_repay_ratio`
- `num_liquidations`
- `redeem_to_mint_ratio`
- `token_diversity`
- `active_days`
- `num_transactions`

## Scoring Logic

The score is computed as a weighted sum of normalized features:

Score =
  0.25 * borrow_repay_ratio +
  0.15 * total_repays +
  0.10 * num_transactions +
  0.10 * token_diversity +
  0.10 * (1 - redeem_to_mint_ratio) +
  0.15 * (1 - num_liquidations) +
  0.15 * active_days

The final score is scaled to a range between 0 and 1000.

## How to Run

1. Add wallet addresses to `data/wallets.txt`
2. Run the script:
```bash
python src/risk_score_generator.py
```

3. Output will be saved to: `output/wallet_scores.csv`
