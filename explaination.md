This project simulates a credit risk scoring model for Ethereum wallets interacting with the Compound V2 protocol. The goal is to identify wallets that show signs of healthy borrowing behavior (e.g., regular repayments, low liquidation, activity diversity) versus risky behavior (e.g., frequent liquidations, minimal repayment, single-token usage).

The features are derived from transaction types such as mint, borrow, repayBorrow, redeem, and liquidateBorrow. Each wallet's behavior is quantified using these features, normalized, and weighted to compute a final risk score between 0 and 1000 — where higher scores represent lower risk.

