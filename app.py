import json,csv,os
from datetime import date
FILE="expenses.json"
def load():
    try:return json.load(open(FILE,encoding="utf-8"))
    except:return []
def save(items):json.dump(items,open(FILE,"w",encoding="utf-8"),indent=2)
def main():
    items=load()
    while True:
        print("\nEXPENSE TRACKER | 1 Add 2 List 3 Summary 4 CSV 0 Exit")
        c=input("> ").strip()
        if c=="1":
            item={"date":input("Date [YYYY-MM-DD]: ") or str(date.today()),"category":input("Category: "),"description":input("Description: "),"amount":float(input("Amount: "))}
            items.append(item);save(items);print("Saved.")
        elif c=="2":
            for i,x in enumerate(items,1):print(i,x["date"],x["category"],x["description"],f'Rp{x["amount"]:,.0f}')
        elif c=="3":
            total=sum(x["amount"] for x in items);cats={}
            for x in items:cats[x["category"]]=cats.get(x["category"],0)+x["amount"]
            print("Total:",f"Rp{total:,.0f}");[print(k,f"Rp{v:,.0f}") for k,v in sorted(cats.items(),key=lambda z:-z[1])]
        elif c=="4":
            with open("expenses.csv","w",newline="",encoding="utf-8") as f:
                w=csv.DictWriter(f,fieldnames=["date","category","description","amount"]);w.writeheader();w.writerows(items)
            print("Exported expenses.csv")
        elif c=="0":break
if __name__=="__main__":main()
