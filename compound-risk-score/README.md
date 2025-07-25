# Compound V2 Wallet Risk Scoring

Assigns a credit risk score (0–1000) to wallets based on Compound V2 transaction history.

## Features Used
- total_borrows
- total_repays
- borrow_repay_ratio
- num_liquidations
- redeem_to_mint_ratio
- token_diversity
- active_days
- num_transactions

## Scoring Logic
Weighted sum of normalized features. Higher score = safer wallet.

## How to Run

1. Add wallet addresses to `data/wallets.txt`
2. Run the script:
```bash
python src/risk_score_generator.py
```

3. Output: `output/wallet_scores.csv`
