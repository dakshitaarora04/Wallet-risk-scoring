import requests
import json
import time
from typing import Dict, List, Any
import pandas as pd
from wallet_addresses import get_wallet_addresses

class CompoundDataFetcher:
    def __init__(self):
        self.compound_v2_url="https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2"
        
        self.wallet_addresses=get_wallet_addresses()
        print(f"Loaded {len(self.wallet_addresses)} wallet addresses from provided list")
    
    def fetch_account_data(self,address:str)->Dict[str,Any]:
        """Fetch account data for a specific wallet address"""
        query = """
        query GetAccount($id:ID!){
            account(id:$id){
                id
                hasBorrowed
                health
                totalBorrowValueInEth
                totalCollateralValueInEth
                countLiquidated
                countLiquidator
                tokens{
                    id
                    symbol
                    cTokenBalance
                    totalUnderlyingSupplied
                    totalUnderlyingBorrowed
                    totalUnderlyingRedeemed
                    totalUnderlyingRepaid
                    accountBorrowIndex
                    totalUnderlyingBorrowedInEth
                    totalUnderlyingSuppliedInEth
                }
            }
        }
        """
        
        variables={"id":address.lower()}
        
        try:
            response=requests.post(
                self.compound_v2_url,
                json={"query":query,"variables":variables},
                timeout=30
            )
            
            if response.status_code==200:
                data=response.json()
                if 'errors' in data:
                    print(f"GraphQL errors for {address[:10]}...: {data['errors']}")
                    return None
                return data.get('data',{}).get('account')
            else:
                print(f"HTTP error {response.status_code} for {address[:10]}...")
                return None
                
        except Exception as e:
            print(f"Error fetching data for {address[:10]}...: {str(e)}")
            return None
    
    def fetch_transaction_history(self, address:str)->Dict[str,Any]:
        
        query = """
        query GetTransactions($account: String!){
            mintEvents(where:{to:$account}, orderBy: blockTime,orderDirection:desc,first:100){
                id
                amount
                to
                from
                blockNumber
                blockTime
                cToken {
                    symbol
                    underlyingSymbol
                }
            }
            redeemEvents(where:{to:$account},orderBy:blockTime,orderDirection:desc,first:100){
                id
                amount
                to
                from
                blockNumber
                blockTime
                cToken{
                    symbol
                    underlyingSymbol
                }
            }
            borrowEvents(where:{borrower: $account},orderBy: blockTime,orderDirection: desc,first: 100) {
                id
                amount
                borrower
                blockNumber
                blockTime
                cToken {
                    symbol
                    underlyingSymbol
                }
            }
            repayEvents(where: {borrower: $account}, orderBy: blockTime, orderDirection: desc, first: 100) {
                id
                amount
                borrower
                payer
                blockNumber
                blockTime
                cToken {
                    symbol
                    underlyingSymbol
                }
            }
            liquidationEvents(where: {borrower: $account}, orderBy: blockTime, orderDirection: desc, first: 50) {
                id
                amount
                borrower
                liquidator
                blockNumber
                blockTime
                cTokenBorrowed {
                    symbol
                    underlyingSymbol
                }
                cTokenCollateral{
                    symbol
                    underlyingSymbol
                }
            }
        }
        """
        
        variables={"account":address.lower()}
        
        try:
            response=requests.post(
                self.compound_v2_url,
                json={"query": query,"variables":variables},
                timeout=30
            )
            
            if response.status_code==200:
                data=response.json()
                if 'errors' in data:
                    print(f"Transaction query errors for {address[:10]}...: {data['errors']}")
                    return {}
                return data.get('data',{})
            else:
                print(f"HTTP error {response.status_code} for transactions {address[:10]}...")
                return {}
                
        except Exception as e:
            print(f"Error fetching transactions for {address[:10]}...: {str(e)}")
            return {}
    
    def fetch_all_wallet_data(self)->Dict[str,Any]:
        
        all_data={}
        
        print(f"\nStarting data fetch for {len(self.wallet_addresses)} wallets")
        print("Estimated time: 3-5 minutes (with API rate limiting)")
        print(" Fetching from The Graph Protocol - Compound V2 Subgraph")
        print("-" * 60)
        
        successful_fetches=0
        failed_fetches=0
        
        for i, address in enumerate(self.wallet_addresses):
            print(f"Processing wallet {i+1}/{len(self.wallet_addresses)}:{address[:10]}")
            
           
            account_data=self.fetch_account_data(address)
            
           
            transaction_data=self.fetch_transaction_history(address)
            
            all_data[address]={
                "account":account_data,
                "transactions":transaction_data,
                "fetch_timestamp":int(time.time())
            }
            
            if account_data is not None:
                successful_fetches+=1
                print(f"Success - Account data retrieved")
            else:
                failed_fetches+=1
                print(f"No account data found (may be inactive wallet)")
            
            
            time.sleep(0.8) 
            
            
            if (i + 1) % 10 == 0:
                print(f"\n Progress: {i + 1}/{len(self.wallet_addresses)} wallets completed")
                print(f" Successful: {successful_fetches} |   No data: {failed_fetches}")
                print("-" * 40)
        
        print(f"\n Data fetch completed")
        print(f" Successfully fetched: {successful_fetches}/{len(self.wallet_addresses)} wallets")
        print(f"  No data found: {failed_fetches}/{len(self.wallet_addresses)} wallets")
        
        return all_data
    
    def save_data(self,data:Dict[str,Any],filename: str="data/compound_wallet_data.json"):
        
        import os
        os.makedirs(os.path.dirname(filename),exist_ok=True)
        
        with open(filename,'w') as f:
            json.dump(data,f,indent=2)
        
        print(f" Data saved to {filename}")
        
        
        timestamp=int(time.time())
        backup_filename=f"data/compound_wallet_data_backup_{timestamp}.json"
        with open(backup_filename, 'w') as f:
            json.dump(data,f,indent=2)
        print(f"💾 Backup saved to {backup_filename}")

def main():
    fetcher = CompoundDataFetcher()
    
    print("COMPOUND PROTOCOL DATA FETCHER")
    print("=" * 50)
    print(f"Target wallets:{len(fetcher.wallet_addresses)}")
    print("Data source:The Graph Protocol - Compound V2")
    print("=" * 50)
    
    
    wallet_data=fetcher.fetch_all_wallet_data()
    
    
    fetcher.save_data(wallet_data)
    
    
    active_wallets=sum(1 for data in wallet_data.values() if data.get('account') is not None)
    print(f"\n DATA FETCH COMPLETED!")
    print(f" Total wallets processed: {len(wallet_data)}")
    print(f" Active wallets found: {active_wallets}")
    print(f" Data saved to: data/compound_wallet_data.json")
    print(f" Ready for risk scoring analysis!")

if __name__ == "__main__":
    main()
