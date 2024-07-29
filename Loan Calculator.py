# Written by Yao-Jen Lee
# Date: 2/3/2024
# Loan Calculator

def loan_calculator(amount,rate,years): # Function for calculate the loan

    monthrate=rate/100/12
    months=years*12
    
    monthpay=(monthrate*amount)/(1-(1+monthrate)**-months)

    total=monthpay*months
    grow=total-amount

    outfile=open('loan_summary.csv','w')
    outfile.write('Prepared by Yao-Jen Lee\n')
    outfile.write('Payment Number, Payment, Interest, Principal, Balance, Total Interest\n')
    formatStr='{:2},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}\n'

    balance=amount
    totinterest=0
   
    for x in range(0,months):
        

        interest=monthrate*balance
        principal=monthpay-interest
        balance=balance-principal
        
        totinterest+=interest
        
        
        outfile.write(formatStr.format((x+1),monthpay,interest,principal,balance,totinterest))
                 
    outfile.close()

    printstr='If you had ${:,.2f} in loans at {:,.1f}% and a {:2}-year term, your monthly payments would be ${:,.2f}. Over the life of your loan, you would repay a total of ${:,.2f}; interest charges would cause your balance to grow by ${:,.2f}'

    
    print('Loan Summary\n')
    print(printstr.format(amount,rate,years,monthpay,total,grow),'\n')
    print('To view monthly detail go to_loan_summary.csv')
    return('Thanks for using the loan calculator!')

