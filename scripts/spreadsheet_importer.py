
import requests
import csv
from io import StringIO
from typing import List

def import_from_google_sheets(sheet_url:str)->List[str]:
    
   
    if '/edit' in sheet_url:
        csv_url=sheet_url.replace('/edit#gid=0','/export?format=csv&gid=0')
        csv_url=csv_url.replace('/edit?usp=sharing','/export?format=csv')
        csv_url=csv_url.replace('/edit','/export?format=csv')
    else:
        csv_url=sheet_url +'/export?format=csv'
    
    try:
        print(f"Fetching data from: {csv_url}")
        response=requests.get(csv_url)
        response.raise_for_status()
        
        
        csv_data=StringIO(response.text)
        reader=csv.DictReader(csv_data)
        
        wallet_addresses=[]
        for row in reader:
            
            wallet_id=row.get('wallet_id') or row.get('Wallet_id') or list(row.values())[0]
            if wallet_id and wallet_id.startswith('0x'):
                wallet_addresses.append(wallet_id.strip())
        
        print(f"Successfully imported {len(wallet_addresses)} wallet addresses")
        return wallet_addresses
        
    except Exception as e:
        print(f" Error importing from Google Sheets: {str(e)}")
        print("Please ensure the Google Sheet is publicly accessible")
        return []

def save_addresses_to_file(addresses:List[str], filename:str ="scripts/wallet_addresses.py"):
    
    
    addresses_str='[\n'
    for addr in addresses:
        addresses_str+=f'    "{addr}",\n'
    addresses_str+=']'
    
    file_content=f'''"""
Wallet addresses imported from Google Sheets
Total addresses: {len(addresses)}
"""

WALLET_ADDRESSES={addresses_str}

def get_wallet_addresses():
    
    return WALLET_ADDRESSES

def validate_addresses():
   
    valid_addresses = []
    invalid_addresses = []
    
    for addr in WALLET_ADDRESSES:
        if addr.startswith('0x') and len(addr) == 42:
            valid_addresses.append(addr.lower())
        else:
            invalid_addresses.append(addr)
    
    print(f"Valid addresses:{{len(valid_addresses)}}")
    print(f"Invalid addresses:{{len(invalid_addresses)}}")
    
    if invalid_addresses:
        print("Invalid addresses found:")
        for addr in invalid_addresses:
            print(f" {{addr}}")
    
    return valid_addresses,invalid_addresses

if __name__=="__main__":
    valid, invalid=validate_addresses()
    print(f"\\nTotal addresses to analyze: {{len(valid)}}")
'''
    
    with open(filename,'w') as f:
        f.write(file_content)
    
    print(f" Addresses saved to {filename}")

def main():
    
    sheet_url="https://docs.google.com/spreadsheets/d/1ZzaeMgNYnxvriYYpe8PE7uMEblTI0GV5GIVUnsP-sBs/edit?usp=sharing"
    
    print("Importing wallet addresses from Google Sheets")
    addresses=import_from_google_sheets(sheet_url)
    
    if addresses:
        print(f"Found {len(addresses)} wallet addresses")
        print("Sample addresses:")
        for i, addr in enumerate(addresses[:5]):
            print(f"  {i+1}. {addr}")
        if len(addresses)>5:
            print(f" and {len(addresses) - 5} more")
        

        save_addresses_to_file(addresses)
        
    
        print("\n Validating addresses")
        valid_count=sum(1 for addr in addresses if addr.startswith('0x') and len(addr)==42)
        print(f" {valid_count}/{len(addresses)} addresses are valid Ethereum addresses")
        
    else:
        print(" No addresses found. Please check the Google Sheets URL and permissions.")

if __name__=="__main__":
    main()
