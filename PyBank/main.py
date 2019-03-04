# Import the libraries

import csv
import os


# Initiatilize the variables used in the program.  Initialize integers = 0 and strings = "".

# Initialize
current_value = 0
prior_value = 0
max_profit=0
max_profit_month = " "
max_loss = 0000000 
average_PnL = 0
numRows =0
total = 0
numRows = 0    
greatest_inc_pr=0 
greatest_dec_pr=0 
total_change =0
fin_analysis_txt =[]
msg=[]
print_msg=" "


# Identify path for print output file

fin_analysis_txt = os.path.join(".","Resources","financial_analysis.txt")

# capture the path of soure file

csvfile = os.path.join( "Resources", "budget_data.csv") 

with open(csvfile, newline="") as csvfile:

#  Create the file reader 

# Reading the rows in the file
    csvreader = csv.reader(csvfile)

# Remove the header  
    next(csvreader)

    for row in csvreader:
    
# Assign the value of profit/loss for the first record into a current_value variable from the file reader.
        current_value = int(row[1])

        if int(row[1]) > max_profit:
            max_profit = int(row[1])
            max_profit_month = (row[0])
            greatest_inc_pr= current_value - prior_value
            #print(prior_value)

        if int(row[1]) < max_loss:
            max_loss = int(row[1])
            max_loss_month = (row[0])
            greatest_dec_pr = current_value - prior_value
            #print("-----")
            #print(prior_value)

        total += int(row[1])
        #print(row[0])
        
        #'${:,.2f}'.format(total)
        #total = '${}'.format(total)
        
        if row[0]!="Jan-10":
            total_change = total_change+ (current_value - prior_value)

        numRows += 1
        prior_value = current_value

    # Formating the values for printing and exporting to file

    average_PnL = total_change/(numRows-1)
    average_PnL = '${:.2f}'.format(average_PnL)
    total = '${}'.format(total)
    greatest_inc_pr = '${}'.format(greatest_inc_pr)
    greatest_dec_pr = '${}'.format(greatest_dec_pr )

    msg.append(f' -------------------------')
    msg.append(f'     Financial Analysis ')
    msg.append(f'------------------------')
    msg.append(f' Total Months:   {numRows}')
    msg.append(f' Total       :   {total}') 
    msg.append(f' Average Change: '+ str(average_PnL) )
    msg.append(f' Greatest Increase in Profits:  '+ str(max_profit_month) + "  (" + str(greatest_inc_pr)+")")
    msg.append(f' Greatest Decrease in Profits: ' + str(max_loss_month) +   "  (" + str(greatest_dec_pr)+")")         
    msg.append(f'------------------------')

   # loop to print out the messages to terminal and text file (financial_analysis.txt) in the 'Resources" directory

with open(fin_analysis_txt,'w') as textfile:
    for print_msg in msg:
        print(print_msg)
        textfile.write(print_msg)
        textfile.write("\n")
