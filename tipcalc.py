def tipCalc(totalBillInput, serviceQual):
    ErrorMessage = 'Whoops! Something went wrong. Please try again by entering the information exactly as it is asked in the prompt.'
    
    finalAmount = 0
    finalTip = 0

    highTip = totalBillInput * .2
    midTip = totalBillInput * .15
    lowTip = totalBillInput * .1

    if serviceQual == 'good':
        #print('Tip amount: $ %.2f' % (highTip))
        #print('Total amount: $ %.2f' % (totalBillInput + highTip))
        finalAmount = totalBillInput + highTip
        finalTip = highTip
    elif serviceQual == 'fair':
        #print('Tip amount: $%.2f' % (midTip))
        #print('Total amount: $%.2f' % (totalBillInput + midTip))
        finalAmount = totalBillInput + midTip
        finalTip = midTip
    elif serviceQual == 'bad':
        #print('Tip amount: $%.2f' % (lowTip))
        #print('Total amount: $%.2f' % (totalBillInput + lowTip))
        finalAmount = totalBillInput + lowTip
        finalTip = lowTip
    else:
        print(ErrorMessage)
        tipCalc(totalBillInput, serviceQual)
    
    return (finalTip, finalAmount)

def tipCalcUI():

    totalBillInput = float(input('How much was your bill (without the $ sign please)? '))
    serviceQual = (input('Was the quality of your service good, fair, or bad? ')).lower()
    tip, total = tipCalc(totalBillInput, serviceQual)
    print('Tip amount: $ %.2f' % (tip))
    print('Total amount: $ %.2f' % (total))

