# MOVIE TICKET PRICING
# MOVIE TICKET ARE PRICED BASED ON THE AGE : $12 FOR ADULTS (18 AND OVER) ,$8 FOR CHILDREN.EVERYONE GETS 
# $2 DISCOUNT ON WEDNESDAY

age = 5
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2

print("Ticket Price for you is $",price)