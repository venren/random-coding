import math
import numpy as np
# A factory produces 1,000 products per day. On average, 2% of the products are defective. 
# If you randomly pick a product, what is the probability that it is defective? 
# If you pick 5 products, what is the probability that at least one is defective?

def prob1():
    no_defective = math.perm(980, 5)
    prob_choosing_5 = math.perm(1000, 5)
    prob_no_defects = no_defective / prob_choosing_5 
    ##print(prob_choosing_5)
    return 1-prob_no_defects

# A marketing company is running an email campaign where they send promotional emails to customers. 
# It is known that the probability of a customer clicking the link in the email (success) is 0.15. 
# The company sends out emails to 100 customers.

# a) What is the probability that exactly 20 customers click the link in the email?
# b) What is the probability that at least 15 customers click the link in the email?

def prob2_a():
    prob_success = 0.15
    combination_click = math.comb(100,20)
    return combination_click * (prob_success ** 20) * ((1-prob_success) ** 80)

def prob2_b():
    total_mail = 100
    prob_success = 0.15
    prob_failure = 1-prob_success
    probablity_till_15_clicks = 0;

    for i in range(0,15):
        bin_coeff = math.comb(total_mail,i)
        probablity_till_15_clicks += (bin_coeff * (prob_success ** i) * (prob_failure ** (total_mail - i)))

    return 1-probablity_till_15_clicks

# 2. Manufacturing Quality Control
# In a factory, the probability that a randomly selected product is defective is 0.02. The company randomly selects 15 products for quality control.

# a) What is the probability that exactly 2 products are defective?
# b) What is the probability that no more than 3 products are defective?
# c) If 3 defective products are found, what is the probability that the total number of defective products is more than 3?

def prob_3_a():
    prob_failure = 0.02
    prob_success = 1-0.02
    bin_coeff = math.comb(15,2)
    return bin_coeff * (prob_failure ** 2) * ((prob_success) ** 13)

def prob_3_b():
    prob_failure = 0.02
    prob_success = 1-prob_failure
    prob_more_than_3  = 0

    for i in range(4,16):
        bin_coeff = math.comb(15,i)
        prob = bin_coeff * (prob_failure ** i) * ((prob_success) ** (15-i))
        print(f"{i} - {prob}")
        prob_more_than_3  += prob

    return 1- prob_more_than_3

print(prob_3_b())