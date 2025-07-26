import json
import random
import time
from typing import Dict, List, Any

class DemoDataGenerator:
    def __init__(self):
        
        self.demo_wallets=[
            "0x0039f22efb07a647557c7c5d17854cfd6d489ef3",
            "0x06b51c6882b27cb05e712185531c1f74996dd988", 
            "0x0795732aacc448030ef374374eaae57d2965c16c",
            "0x0aaa79f1a86bc8136cd0d1ca0d519644fe3766f9",
            "0x111c7208a7e2af345d36b6d4aace8740d61a3078",
            "0x124853fecb522c57d9bd5c21231058696ca6d696",
            "0x13b1c8b0e696af8b4fee742119b549b605f3cbc",
            "0x1656f1886c5ab634ac19568cd57bc72f385fdf7",
            "0x0fe383e5abc200055a71391f94a5f541f844b9ae",
            "0x104ae61dd4487ad689969a17807ddc338b445416",
        ]
        
        self.token_symbols=["cDAI","cUSDC","cETH","cWBTC","cUNI","cCOMP","cAAVE"]
        self.underlying_symbols=["DAI","USDC","ETH","WBTC","UNI","COMP","AAVE"]
    
    def generate_account_data(self,wallet_address:str,risk_profile:str)->Dict[str,Any]:
        
        
        if risk_profile=="very_low":
            return {
                "id":wallet_address.lower(),
                "hasBorrowed":False,
                "health":"5.2",
                "totalBorrowValueInEth":"0",
                "totalCollateralValueInEth":"2.5",
                "countLiquidated":0,
                "countLiquidator":0,
                "tokens":self._generate_tokens(2,"conservative")
            }
        elif risk_profile=="low":
            return {
                "id":wallet_address.lower(),
                "hasBorrowed":True,
                "health":"2.8",
                "totalBorrowValueInEth":"1.2",
                "totalCollateralValueInEth":"4.5",
                "countLiquidated":0,
                "countLiquidator":0,
                "tokens":self._generate_tokens(3,"conservative")
            }
        elif risk_profile=="medium":
            return {
                "id":wallet_address.lower(),
                "hasBorrowed":True,
                "health":"1.6",
                "totalBorrowValueInEth":"3.2",
                "totalCollateralValueInEth":"5.8",
                "countLiquidated":random.randint(0,1),
                "countLiquidator":0,
                "tokens":self._generate_tokens(4,"moderate")
            }
        elif risk_profile=="high":
            return {
                "id":wallet_address.lower(),
                "hasBorrowed":True,
                "health":"1.15",
                "totalBorrowValueInEth":"6.8",
                "totalCollateralValueInEth":"8.2",
                "countLiquidated":random.randint(1,3),
                "countLiquidator":0,
                "tokens":self._generate_tokens(2,"aggressive")
            }
        else:  
            return {
                "id":wallet_address.lower(),
                "hasBorrowed":True,
                "health":"1.05",
                "totalBorrowValueInEth":"9.2",
                "totalCollateralValueInEth":"10.1",
                "countLiquidated":random.randint(3,6),
                "countLiquidator":0,
                "tokens":self._generate_tokens(1,"very_aggressive")
            }
    
    def _generate_tokens(self,count:int,style:str,wallet_address:str)->List[Dict[str,Any]]:
        
        tokens=[]
        selected_tokens=random.sample(list(zip(self.token_symbols,self.underlying_symbols)),count)
        
        for i, (symbol, underlying) in enumerate(selected_tokens):
            if style=="conservative":
                supplied=round(random.uniform(0.5,2.0),4)
                borrowed=round(random.uniform(0,supplied * 0.3), 4) if random.random()>0.3 else 0
            elif style=="moderate":
                supplied=round(random.uniform(1.0,3.0),4)
                borrowed=round(random.uniform(0, supplied * 0.6), 4) if random.random()>0.2 else 0
            elif style=="aggressive":
                supplied=round(random.uniform(2.0, 5.0),4)
                borrowed=round(random.uniform(supplied * 0.4, supplied * 0.8),4)
            else: 
                supplied=round(random.uniform(3.0,8.0),4)
                borrowed=round(random.uniform(supplied * 0.7, supplied * 0.95),4)
            
            tokens.append({
                "id": f"{wallet_address.lower()}-{symbol.lower()}",
                "symbol":symbol,
                "cTokenBalance":str(random.uniform(100, 10000)),
                "totalUnderlyingSupplied":str(supplied * random.uniform(0.8,1.2)),
                "totalUnderlyingBorrowed":str(borrowed),
                "totalUnderlyingRedeemed":str(random.uniform(0,supplied * 0.5)),
                "totalUnderlyingRepaid":str(random.uniform(0,borrowed * 1.2)),
                "accountBorrowIndex":str(random.uniform(1.0,1.5)),
                "totalUnderlyingBorrowedInEth":str(borrowed),
                "totalUnderlyingSuppliedInEth":str(supplied)
            })
        
        return tokens
    
    def generate_transaction_events(self,wallet_address: str,risk_profile:str)->Dict[str,List[Dict[str,Any]]]:
       
        
        base_time=int(time.time())-(365 * 24 * 3600)  
        
        if risk_profile=="very_low":
            mint_count=random.randint(2,5)
            redeem_count=random.randint(0,2)
            borrow_count=0
            repay_count=0
            liquidation_count=0
        elif risk_profile=="low":
            mint_count=random.randint(5,12)
            redeem_count=random.randint(2,6)
            borrow_count=random.randint(3,8)
            repay_count=random.randint(3,10)
            liquidation_count=0
        elif risk_profile=="medium":
            mint_count=random.randint(10,25)
            redeem_count=random.randint(5,15)
            borrow_count=random.randint(8,20)
            repay_count=random.randint(6,18)
            liquidation_count=random.randint(0,1)
        elif risk_profile=="high":
            mint_count=random.randint(15,40)
            redeem_count=random.randint(10,25)
            borrow_count=random.randint(20,45)
            repay_count=random.randint(10,30)  
            liquidation_count=random.randint(1,3)
        else: 
            mint_count=random.randint(20,60)
            redeem_count=random.randint(15,35)
            borrow_count=random.randint(30,70)
            repay_count=random.randint(5,25)  
            liquidation_count=random.randint(3,6)
        
        return {
            "mintEvents":self._generate_mint_events(mint_count,wallet_address,base_time),
            "redeemEvents":self._generate_redeem_events(redeem_count,wallet_address,base_time),
            "borrowEvents":self._generate_borrow_events(borrow_count,wallet_address,base_time),
            "repayEvents":self._generate_repay_events(repay_count,wallet_address,base_time),
            "liquidationEvents":self._generate_liquidation_events(liquidation_count,wallet_address,base_time)
        }
    
    def _generate_mint_events(self,count:int,wallet_address:str,base_time:int)->List[Dict[str,Any]]:
        events=[]
        for i in range(count):
            token_idx=random.randint(0,len(self.token_symbols)-1)
            events.append({
                "id": f"mint-{wallet_address}-{i}",
                "amount":str(random.uniform(0.1,5.0)),
                "to":wallet_address.lower(),
                "from":"0x0000000000000000000000000000000000000000",
                "blockNumber":str(random.randint(15000000,18000000)),
                "blockTime":str(base_time + random.randint(0, 365 * 24 * 3600)),
                "cToken":{
                    "symbol":self.token_symbols[token_idx],
                    "underlyingSymbol":self.underlying_symbols[token_idx]
                }
            })
        return events
    
    def _generate_redeem_events(self,count: int,wallet_address:str,base_time:int)->List[Dict[str,Any]]:
        events=[]
        for i in range(count):
            token_idx=random.randint(0,len(self.token_symbols)-1)
            events.append({
                "id":f"redeem-{wallet_address}-{i}",
                "amount":str(random.uniform(0.05,2.0)),
                "to":wallet_address.lower(),
                "from":wallet_address.lower(),
                "blockNumber":str(random.randint(15000000,18000000)),
                "blockTime":str(base_time+random.randint(0,365 * 24 * 3600)),
                "cToken":{
                    "symbol":self.token_symbols[token_idx],
                    "underlyingSymbol":self.underlying_symbols[token_idx]
                }
            })
        return events
    
    def _generate_borrow_events(self,count:int,wallet_address:str,base_time:int)->List[Dict[str,Any]]:
        events=[]
        for i in range(count):
            token_idx=random.randint(0,len(self.token_symbols)-1)
            events.append({
                "id":f"borrow-{wallet_address}-{i}",
                "amount":str(random.uniform(0.1,3.0)),
                "borrower":wallet_address.lower(),
                "blockNumber":str(random.randint(15000000,18000000)),
                "blockTime":str(base_time + random.randint(0,365 * 24 * 3600)),
                "cToken":{
                    "symbol":self.token_symbols[token_idx],
                    "underlyingSymbol":self.underlying_symbols[token_idx]
                }
            })
        return events
    
    def _generate_repay_events(self,count: int,wallet_address:str,base_time:int)->List[Dict[str,Any]]:
        events=[]
        for i in range(count):
            token_idx=random.randint(0,len(self.token_symbols)-1)
            events.append({
                "id":f"repay-{wallet_address}-{i}",
                "amount":str(random.uniform(0.05,2.5)),
                "borrower":wallet_address.lower(),
                "payer":wallet_address.lower(),
                "blockNumber":str(random.randint(15000000,18000000)),
                "blockTime":str(base_time+random.randint(0,365 *24 *3600)),
                "cToken":{
                    "symbol":self.token_symbols[token_idx],
                    "underlyingSymbol":self.underlying_symbols[token_idx]
                }
            })
        return events
    
    def _generate_liquidation_events(self,count:int,wallet_address:str,base_time:int)->List[Dict[str,Any]]:
        events=[]
        for i in range(count):
            borrow_token_idx=random.randint(0,len(self.token_symbols)-1)
            collateral_token_idx=random.randint(0,len(self.token_symbols)-1)
            events.append({
                "id":f"liquidation-{wallet_address}-{i}",
                "amount":str(random.uniform(0.5,4.0)),
                "borrower":wallet_address.lower(),
                "liquidator":f"0x{''.join(random.choices('0123456789abcdef',k=40))}",
                "blockNumber":str(random.randint(15000000,18000000)),
                "blockTime":str(base_time + random.randint(0, 365 * 24 * 3600)),
                "cTokenBorrowed":{
                    "symbol":self.token_symbols[borrow_token_idx],
                    "underlyingSymbol":self.underlying_symbols[borrow_token_idx]
                },
                "cTokenCollateral":{
                    "symbol":self.token_symbols[collateral_token_idx],
                    "underlyingSymbol":self.underlying_symbols[collateral_token_idx]
                }
            })
        return events
    
    def generate_demo_data(self)->Dict[str,Any]:
        
        risk_profiles=["very_low","low","medium","medium","very_high","high","medium","low","high","medium"]
        
        demo_data = {}
        
        print("Generating realistic demo data for 10 wallets")
        
        for i,(wallet_address, risk_profile) in enumerate(zip(self.demo_wallets, risk_profiles)):
            print(f" Generating wallet {i+1}/10: {wallet_address[:10]}... ({risk_profile} risk)")
            
            account_data=self.generate_account_data(wallet_address,risk_profile)
            transaction_data=self.generate_transaction_events(wallet_address,risk_profile)
            
            demo_data[wallet_address]={
                "account":account_data,
                "transactions":transaction_data,
                "fetch_timestamp":int(time.time()),
                "demo_risk_profile":risk_profile  
            }
        
        return demo_data
    
    def save_demo_data(self, data: Dict[str,Any], filename: str = "data/compound_wallet_data.json"):
       
        import os
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename,'w') as f:
            json.dump(data,f,indent=2)
        
        print(f"Demo data saved to {filename}")

def main():
    generator=DemoDataGenerator()
    
    
    demo_data=generator.generate_demo_data()
    
    
    generator.save_demo_data(demo_data)
    
    print(f"\n Demo data generation completed!")
    print(f"Generated data for {len(demo_data)} wallets")
    print(f" Data saved to: data/compound_wallet_data.json")
    print(f"\nRisk profile distribution:")
    
    profiles={}
    for wallet_data in demo_data.values():
        profile=wallet_data["demo_risk_profile"]
        profiles[profile] = profiles.get(profile, 0)+1
    
    for profile, count in profiles.items():
        print(f" {profile.replace('_', ' ').title()}: {count} wallets")

if __name__=="__main__":
    main()
