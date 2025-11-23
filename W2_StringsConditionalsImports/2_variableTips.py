
# ********** Lec 2 [ Variable - TIPS ]

#? Try to make your variables as self-explanatory: ram_loan, ram_bank_balance, ram_net_income
#? Add comments, before closing compiler make sure to add lots of comments, it is a good practice 


ram_bank_balance = 1000000
# ram's bank balance, note that this is positive

ram_loan=200000
# ram's loan, this is to be returned by him and hence will count as negative



laxman_bank_balance = 2300000
# laxman's bank balance, note that this is positive

laxman_loan = 32909
# laxman's loan, this is to be returned by him and hence will count as negative




net_income = ram_bank_balance + laxman_bank_balance
# net_income is the total bank balance of ram's family

net_liability= ram_loan + laxman_loan
# net_liability is the total loan of the family

final_value= net_income - net_liability
# final_value is the family's final money (could be +ve or -ve)
   
