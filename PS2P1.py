#input phase
tickersymb= input("Tickersymbol: ")
shares= float(input("amount of shares" ))
costpershare= float(input("Cost per share of stocks:$"))

#process phase
invested= shares * costpershare

#output phase
print("Stock ticker symbol:",tickersymb )
print("You invested $ ", invested)
