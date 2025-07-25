### Data Collection Method
Used Python (Web3.py or simulation) to fetch wallet interactions with Compound V2 protocol: mint, borrow, repayBorrow, redeem, liquidateBorrow.

### Feature Selection
- total_borrows
- total_repays
- borrow_repay_ratio
- num_liquidations
- redeem_to_mint_ratio
- token_diversity
- active_days
- num_transactions

### Scoring Method
Each feature was normalized (min-max), then scored using:

Score = 
  0.25 * borrow_repay_ratio +
  0.15 * total_repays +
  0.10 * num_transactions +
  0.10 * token_diversity +
  0.10 * (1 - redeem_to_mint_ratio) +
  0.15 * (1 - num_liquidations) +
  0.15 * active_days

Score is scaled to 0–1000.

### Risk Indicators
- High liquidation = high risk
- Low repayment = irresponsible behavior
- Low token diversity = bot-like usage
- Fast deposit-redeem = suspicious churn
