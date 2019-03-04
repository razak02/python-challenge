import csv
import os



# Identify the variables and initialize

voter_id = 000
county = " "
candidate = " "
tot_votes= 000
khan_tot_votes =0
khan_vote_per= 0
cor_tot_votes=0
cor_vote_per=0
li_tot_votes=0
li_vote_per=0
ot_tot_votes=0
ot_vote_per=0
pollsdata={}
winner =" "
output_file = " "
election_results= " "
analysis_txt =[]
msg=[]
print_msg=""

# Identify path for source file

election_file = os.path.join(".","Resources","election_data.csv")

# Identify path for print output file

analysis_txt = os.path.join(".","Resources","election_analysis.txt")

# Open source file for reading 

with open(election_file, 'r') as csvfile:

# read using the csv to dictionary reader 

   reader = csv.DictReader(csvfile, delimiter=',')
 
 # Match the 'Candidate' value to sum up the votes     
      
   for row in reader:
      Candidate = (row["Candidate"])
      Voter_Id = (int(row["Voter ID"]))
      County = (row["County"])
      if "Khan" == Candidate:
         #print (Candidate)
         khan_tot_votes = khan_tot_votes + 1
      if "Li" == Candidate:
         li_tot_votes= li_tot_votes + 1
      if "Correy" == Candidate:    
         cor_tot_votes = cor_tot_votes + 1
      if "O'Tooley" == Candidate:   
         ot_tot_votes = ot_tot_votes +1

   #  Sum up the total votes 
  
      tot_votes = (khan_tot_votes + li_tot_votes + cor_tot_votes +ot_tot_votes)   

   
   # Identifying the  winner

      if li_tot_votes > cor_tot_votes and li_tot_votes > khan_tot_votes and li_tot_votes > ot_tot_votes:
         winner = "Li"
      elif cor_tot_votes > li_tot_votes and cor_tot_votes > khan_tot_votes and cor_tot_votes > ot_tot_votes:
         winner = "Correy"
      elif ot_tot_votes > cor_tot_votes and ot_tot_votes > khan_tot_votes and ot_tot_votes > li_tot_votes:
         winner = "O'Toole"
      elif khan_tot_votes > cor_tot_votes and khan_tot_votes > li_tot_votes and khan_tot_votes > ot_tot_votes:
         winner = "Khan"  


   # Format the percentages for each candidate to three decimals

      li_vote_per = '{0:.3%}'.format(li_tot_votes/tot_votes)
      cor_vote_per = '{0:.3%}'.format(cor_tot_votes/tot_votes)
      ot_vote_per = '{0:.3%}'.format(ot_tot_votes/tot_votes)
      khan_vote_per ='{0:.3%}'.format(khan_tot_votes/tot_votes)


   # Gather Result details messages for printing to file and terminal 
   
   msg.append(f' -------------------------')
   msg.append(f'    Election Results: ')
   msg.append(f'------------------------')
   msg.append(f' Total Votes: ({tot_votes})')
   msg.append(f'------------------------')
   msg.append(f' khan   : '+ str(khan_vote_per) + "   (" + str(khan_tot_votes) + ")")
   msg.append(f' Li     : '+ str(li_vote_per) + "   (" + str(li_tot_votes) + ")")
   msg.append(f' Correy : '+ str(cor_vote_per) + "   (" + str(cor_tot_votes) + ")")
   msg.append(f' O Toole: '+ str(ot_vote_per) + "   (" + str(ot_tot_votes) + ")")         
   msg.append(f'------------------------')
   msg.append(f'  Winner : ' +str(winner))
   msg.append(f'------------------------')

   # loop to print out the messages to terminal and text file in the 'Resources" directory

   with open(analysis_txt,'w') as textfile:
      for print_msg in msg:
         print(print_msg)
         textfile.write(print_msg)
         textfile.write("\n")

