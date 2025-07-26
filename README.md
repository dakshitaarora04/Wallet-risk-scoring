# Wallet Risk Scoring System - DEMO

**Live Demo of DeFi Wallet Risk Assessment**

This demo highlights a risk scoring system that analyzes DeFi wallet behavior patterns to assign risk scores from 0 to 1000.

## Quick Demo

Run the complete demo with one command:



This will:
1. Generate realistic sample data for 10 wallets
2. Calculate risk scores using our 6-factor model  
3. Show detailed results and validation
4. Create all necessary output files

## Demo Features

### Sample Wallets with Different Risk Profiles:
- **Very Low Risk**: Conservative positions, no borrowing
- **Low Risk**: Moderate leverage, good repayment history
- **Medium Risk**: Balanced activity, some concerning patterns
- **High Risk**: High leverage, poor repayment patterns
- **Very High Risk**: Multiple liquidations, critical health factors

### Risk Factors Analyzed:
1. **Liquidation Risk (25%)** - Past liquidations plus health factor
2. **Leverage Risk (20%)** - Debt-to-collateral ratios
3. **Behavioral Risk (20%)** - Transaction patterns
4. **Portfolio Risk (15%)** - Asset diversification
5. **Activity Risk (10%)** - Engagement levels
6. **Repayment Risk (10%)** - Debt management history

## Demo Output Files

After running the demo, you will receive:

```
data/
├── compound_wallet_data.json     # Sample wallet data
└── wallet_risk_scores.csv        # Final CSV (wallet_id, score)

output/
└── detailed_risk_analysis.json   # Complete risk breakdown
```

## Expected Demo Results

The demo checks model accuracy by comparing calculated scores with intended risk profiles:

| Wallet | Demo Profile | Expected Score Range | Calculated Score | Status |
|--------|-------------|---------------------|------------------|---------|
| 0xfaa... | Very High | 801-1000 | ~850 | Correct |
| 0x742... | Low | 201-400 | ~320 | Correct |
| 0x123... | Medium | 401-600 | ~480 | Correct |

**Expected Accuracy**: ~80-90% (model correctly categorizes most wallets)

## Sample Output

```
INDIVIDUAL WALLET SCORES:
Wallet Address                               Score  Category          Demo Profile
---------------------------------------------------------------------------------
0xabcdef123456789abcdef123456789abcdef1234c  156    Very Low Risk     Very Low    
0x742d35cc6634c0532925a3b8d0c9e3e0c0e8c8e8  287    Low Risk          Low         
0x123456789abcdef123456789abcdef123456789a  463    Medium Risk       Medium      
0xfaa0768bde629806739c3a4620656c5d26f44ef2  847    Very High Risk    Very High   

SUMMARY STATISTICS:
Total wallets processed: 10
Average risk score: 485.2
Median risk score: 456.0
Min risk score: 156
Max risk score: 847

Model Accuracy: 8/10 (80.0%)
```

## Individual Demo Scripts

### Generate Sample Data Only:
```bash
python scripts/demo_data_generator.py
```

### Calculate Scores Only (requires data):
```bash
python scripts/wallet_risk_calculator.py
```

## From Demo to Production

To use with real data:

1. Replace `demo_data_generator.py` with `compound_data_fetcher.py`
2. Add your 100 real wallet addresses
3. Configure The Graph API endpoints
4. Run the same risk calculation process

## Customization Options

### Adjust Risk Weights:
```python
self.weights = {
    "liquidation_risk": 0.30,    # Increase liquidation focus
    "leverage_risk": 0.25,       # Increase leverage sensitivity
    "behavioral_risk": 0.20,     # Keep behavioral analysis
    "portfolio_risk": 0.15,      # Keep diversification focus
    "activity_risk": 0.05,       # Reduce activity weight
    "repayment_risk": 0.05       # Reduce repayment weight
}
```

### Modify Risk Thresholds:
Edit the scoring logic in individual risk calculation methods.

## Demo Validation

The demo includes built-in validation:
- Data Generation: Creates realistic transaction patterns
- Score Calculation: Applies all 6 risk factors correctly  
- Result Validation: Compares calculated versus expected scores
- Output Format: Generates required CSV and JSON files

## Demo Limitations

This demo uses:
- Simulated data (not real blockchain transactions)
- 10 wallets (compared to 100 in production)
- Simplified patterns (real data is more complex)
- No API calls (ensures faster execution)

## Key Takeaways

1. The model works and successfully differentiates between risk levels.
2. It has a scalable design that easily extends to over 100 wallets.
3. The analysis is thorough with a 6-factor approach that captures various risk aspects.
4. The output is clear, available in both CSV and detailed JSON formats.
5. It is customizable; weights and thresholds can be adjusted.

---

