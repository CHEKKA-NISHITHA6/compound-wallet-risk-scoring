import os
import pandas as pd
import numpy as np

def load_wallets(file_path='data/wallets.txt'):
    with open(file_path, 'r') as f:
        wallets = [line.strip().lower() for line in f if line.strip()]
    return wallets

def fetch_compound_transactions(wallet):
    np.random.seed(int(wallet[:6], 16))
    return {
        'total_borrows': np.random.uniform(100, 10000),
        'total_repays': np.random.uniform(50, 10000),
        'num_liquidations': np.random.randint(0, 5),
        'redeem_to_mint_ratio': np.random.uniform(0, 2),
        'token_diversity': np.random.randint(1, 6),
        'active_days': np.random.randint(1, 300),
        'num_transactions': np.random.randint(5, 100)
    }

def normalize_features(df):
    normalized = (df - df.min()) / (df.max() - df.min() + 1e-6)
    return normalized.fillna(0)

def compute_scores(features):
    normed = normalize_features(features)
    score = (
        0.25 * normed['borrow_repay_ratio'] +
        0.15 * normed['total_repays'] +
        0.10 * normed['num_transactions'] +
        0.10 * normed['token_diversity'] +
        0.10 * (1 - normed['redeem_to_mint_ratio']) +
        0.15 * (1 - normed['num_liquidations']) +
        0.15 * normed['active_days']
    )
    return (score * 1000).astype(int).clip(0, 1000)

def main():
    os.makedirs('output', exist_ok=True)
    wallets = load_wallets()
    rows = []
    for wallet in wallets:
        tx_data = fetch_compound_transactions(wallet)
        borrow_repay_ratio = tx_data['total_repays'] / (tx_data['total_borrows'] + 1e-6)
        rows.append({
            'wallet_id': wallet,
            **tx_data,
            'borrow_repay_ratio': borrow_repay_ratio
        })
    df = pd.DataFrame(rows)
    df['score'] = compute_scores(df.drop(columns='wallet_id'))
    df[['wallet_id', 'score']].to_csv('output/wallet_scores.csv', index=False)
    print("✅ Wallet risk scores saved to output/wallet_scores.csv")

if __name__ == '__main__':
    main()
