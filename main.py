from collections import defaultdict
from pprint import pprint
from last_years_taxdata import coin_dict


def main():

    for key in coin_dict:
        coin_dict[key]['basisbasis'] = coin_dict[key]['basis'] * coin_dict[key]['amount']

    # The CSV should be in format "_ COINNAME COINAMOUNT SEKPAID OPERATION"
    # Valid operations are Sale, Loanrepay, Purachse, Stakingreward, Loan,
    with open('CC - 2022.tsv',encoding="utf8") as file:
        lines = file.read().splitlines()
    lines.pop(0)
    for line in lines:
        line = line.replace('kr','').replace(',','.').replace(' ','').replace('−', '-')
        line = line.split('	')
        line = [el.replace('\xa0', "") for el in line]
        coin = line[1]
        coin_amt = float(line[2])
        kr_amt = float(line[3])

            
        if line[4] in ['Sale', 'Loanrepay']:
            basis = coin_dict[coin]['basis']
            coin_dict[coin]['amount'] += coin_amt
            coin_dict[coin]['basisbasis'] += basis * coin_amt
            tax_amt = ( kr_amt - basis * coin_amt )
            coin_dict[coin]['tax'] += 0.3 * tax_amt if tax_amt > 0 else 0.7 * 0.3 * tax_amt
            coin_dict[coin]['basis'] = coin_dict[coin]['basisbasis'] / coin_dict[coin]['amount'] if coin_dict[coin]['amount'] else 0

        if line[4] in ['Purchase', 'Stakingreward', 'Loan', 'Newtoken']:
            coin_dict[coin]['amount'] += coin_amt
            coin_dict[coin]['basisbasis'] += kr_amt
            coin_dict[coin]['basis'] = coin_dict[coin]['basisbasis'] / coin_dict[coin]['amount'] if coin_dict[coin]['amount'] else 0
    tax_total = 0
    for key in coin_dict:
        tax_total += coin_dict[key]['tax']

    pprint(coin_dict)
    print(tax_total)

if __name__ == '__main__':
    main()