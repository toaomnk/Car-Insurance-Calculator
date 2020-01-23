def insurance(age, gender, vehicle, coverage, student, accidents, violations, background, credit):

	print("\nThe following calculator will estimate the cost to insure you based on calculating risk. \n")
	print("There are various factors on which your insurance cost will be affected. Many insurance companies also offer a wide-variety of discounts.")
	print("While it is more ideal to get a quote an insurance company yourself, I hope that this is a valuable learning tool!")

	rate = 100 

	age = int(input("\nPlease enter your age: "))

	if age > 16 and age < 20:
		rate = rate + 50
		print("\nDid you know that after the age of 24, your insurance cost will significantly decrease?")
	elif age >= 20 and age < 24:
		rate = rate + 25
		print("\nDid you know that after the age of 24, your insurance cost will significantly decrease?")
	elif age >= 24 and age < 30:
		rate = rate - 50
	elif age >= 30:
		rate = rate - 65
	elif age < 16:
		raise Exception("\nYou cannot have a drivers permit if you are under the age of 16.")

	print("\n1: Male, 2: Female")

	gender = int(input("\nPlease enter your gender: "))

	if gender == 1:
		rate = rate + 15
		print("\nFun fact: Women tend to have cheaper insurnance than men. Statistics have shown that women tend to be safer drivers than men and are more cautious on the road.")
	elif gender == 2:
		print("\nFun fact: Women tend to have cheaper insurnance than men. Statistics have shown that women tend to be safer drivers than men and are more cautious on the road.")
		pass
	elif gender < 1:
		raise(Exception)
	elif gender > 2:
		raise(Exception)

	print("\n1: 0 - $5,000, 2: $5,000 - 10,000, 3: $10,000 - $15,000, 4: $15,000 - $20,000, 5: $20,000 - $35,000: ")

	vehicle = int(input("\nHow much does your vehicle cost? "))

	if vehicle == 1:
		rate = rate - 50
		print("\nThe more expensive your vehicle is, the more expensive your insurnance will be! Based off of the game of risk, the insurance company has more money to potentially lose the more expensive your car is.")
	elif vehicle == 2:
		rate = rate - 25
		print("\nThe more expensive your vehicle is, the more expensive your insurnance will be! Based off of the game of risk, the insurance company has more money to potentially lose the more expensive your car is.")	
	elif vehicle == 3:
		print("\nThe more expensive your vehicle is, the more expensive your insurnance will be! Based off of the game of risk, the insurance company has more money to potentially lose the more expensive your car is.")
	elif vehicle == 4: 
		rate = rate + 50
		print("\nThe more expensive your vehicle is, the more expensive your insurnance will be! Based off of the game of risk, the insurance company has more money to potentially lose the more expensive your car is.")
	elif vehicle == 5:
		rate = rate + 75
		print("\nThe more expensive your vehicle is, the more expensive your insurnance will be! Based off of the game of risk, the insurance company has more money to potentially lose the more expensive your car is.")
	elif vehicle < 1:
		raise Exception("An imvalid value was entered.")
	elif vehicle > 5:
		raise Exception("An invalid value was entered.")

	accidents = int(input("\nHow many accidents have you been involved in? "))

	if accidents < 0:
		raise(Exception)
	elif accidents == 0:
		rate = rate - 15
		print("\nStudies have shown that drivers whom have gotten in an accident before are more likely to get into another one! Keeping a clean record is a good indicator of your driving habits.")
	elif accidents >= 1:
		rate = rate + (accidents * 15)
		print("\nStudies have shown that drivers whom have gotten in an accident before are more likely to get into another one! Keeping a clean record is a good indicator of your driving habits.")
	elif accidents > 5:
		raise Exception("Due to simulation reasons, the calculator will not accept drivers with over than 5 accidents, and neither will some insurance companies.")

	violations = int(input("\nEnter the number of speeding vioaltions you have received: "))

	if violations == 0:
		rate = rate - 15
		print("\nInsurance companies see speeding violations as an increased risk, even if there is only one on your record. This is because if you tend to speed, the more likely you are to get into an accident thus potentially causing the insurnace to lose money.")
	elif violations > 0:
		rate = rate + (15 * violations)
	elif violations < 0: 
		raise(Exception)
	elif violations > 5:
		raise Exception("Due to simulation reasons, the calculator will not accept drivers with over than 5 speeding violations, and niether will some insurance companies.")

	background = int(input("\nAre there any discrepencies on your criminal record? If so, how many are there? Enter 0 for none. : "))

	print("\nWhile having a clean criminal background does not indicate your driving habits, it does show the insurance company that you tend to follow the rules. Many insurance companies offer discounts for having a clean criminal record.")
	if background == 0:
		rate = rate - 10
	elif background > 0:
		rate = rate + (background * 10)

	print("\n1: Liability, 2: Full-Coverage")

	coverage = int(input("\nWhich coverage option would you like? "))

	print("\nFull-Coverage tends to cost significantly more than liability because they will insure a lot more than just you being at-fault in an accident.")
	print("\nFun-fact! If you are financing or leasing a vehicle, you are required to have full-coverage insurance.")

	if coverage == 1:
		pass
	elif coverage == 2:
		rate = rate*2.15
	elif coverage > 2:
		raise Exception("An invalid value was entered.")
	elif coverage <= 0:
		raise Exception("An invalid value was entered.")

	print("\n1: Yes, 2: No")

	student = int(input("\nAre you currently a student with over a 3.0 GPA? "))

	print("\nBeing a good student is a plus to insurance companies because it shows that you know how to follow rules! This is a common discount insurance companies offer, due to many college students having high monthly premiums.")

	if student == 1:
		rate = rate - 15
	elif student == 2:
		pass
	elif student < 0:
		raise Exception("An invalid value was entered.")
	elif student > 2:
		raise Exception("An invalid value was entered.")

	print("\n1: No credit, 2: 0-649, 3: 650-699, 4: 700-749, 5: 750-800, 6: 800+")

	credit = int(input("\nPlease enter your credit range: "))

	print("\nHaving good credit shows that you can pay your bills on time! This gives the insurance company peace of mind with insuring you, and many will also offer a discount for having good credit.")

	if credit == 1:
		rate = rate + 30
	elif credit == 2:
		rate = rate + 25
	elif credit == 3:
		rate = rate + 15
	elif credit == 4:
		pass
	elif credit == 5:
		rate = rate - 15
	elif credit == 6:
		rate = rate - 20
	elif credit < 1:
		raise Exception("An invalid value was entered.")
	elif credit > 6:
		raise Exception("An invalid value was entered.")

	discounts = []
	discount = 0

	if credit == 4:
		discount = 15
		discounts.append("Good Credit")
	elif credit == 5:
		discount = 30
		discounts.append("Good Credit")
	elif credit == 6:
		discount = 50
		discounts.append("Good Credit")
	if student == 1:
		discount = discount + 15
		discounts.append("Good Student")
	if accidents == 0:
		discount = discount + 15
		discounts.append("Zero Accidents")
	if violations == 0:
		discount = discount + 15
		discounts.append("Safe Driver")
	if background == 0:
		discount = discount + 10
		discounts.append("Clean Background")

	if len(discounts) > 0:
		print("\nThe following discount(s) have been applied saving you $%d." % (discount))

	for x in discounts:
		print("-" + x)
	if accidents > 0:
		print("\nRemoving the %d accident(s) on your record could save you up to $%s!" % (accidents, accidents * 15))

	print("\nYour estimated insurnace cost is $%s per month." % (round(rate, 2)))

	if coverage == 1:
		print("\nGet peace of mind with Full-Coverage insurance! It could cost $%d per month.\n" % round(rate * 2.15, 2))
	elif coverage == 2:
		print("\nDowngrading to liability could cost $%s per month.\n" % round(rate / 2.15, 2))

insurance(20, 1, 1, 1, 1, 1, 1, 1, 1)