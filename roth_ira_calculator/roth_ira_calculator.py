# ROTH IRA CALCULATOR BEN MALONE
# This calculator is meant to give a variety of possible values for ROTH IRA outcomes depending on a number of 
# features given by the user. A small algorithm with a randomizer is used along with trends from the past 50 years
# of ROTH IRA annual return rates and interest rates to compute a rough estimate of the current day
# cash value the user will have after a period of time specified by the user
import random

LOW_END_ANNUAL_RETURN_RATE = 1.06
HIGH_END_ANNUAL_RETURN_RATE = 1.1
LOW_END_INFLATION_RATE = 1.03
HIGH_END_INFLATION_RATE = 1.04

def gather_age():
    print("Enter the age you would like to begin investing:")
    start_age = input()
    print("Enter the age you would like to retire:")
    end_age = input()
    return start_age, end_age

def produce_samples(start_age, end_age):
    ret_rate_samples = []
    inf_rate_samples = []
    for i in range(start_age, end_age):
        ret_rate_samples.append(random.uniform(LOW_END_ANNUAL_RETURN_RATE, HIGH_END_ANNUAL_RETURN_RATE))
        inf_rate_samples.append(random.uniform(LOW_END_INFLATION_RATE, HIGH_END_INFLATION_RATE))
    return ret_rate_samples, inf_rate_samples

def generate_p_samples(low_end_principal, high_end_principal_a50, high_end_principal_b50, start_age, end_age):
    principal_samples = []
    for i in range(start_age, end_age):
        if(start_age + i < 50):
            principal_samples.append(random.uniform(low_end_principal, high_end_principal_b50))
        else:
            principal_samples.append(random.uniform(low_end_principal, high_end_principal_a50))
    return principal_samples

def calculate_outcome(ret_rate_samples, inf_rate_samples, principal_samples):
    nominal_value = 0.0
    for i in range(len(ret_rate_samples)):
        nominal_value += principal_samples[i]
        nominal_value *= ret_rate_samples[i]
        nominal_value /= inf_rate_samples[i]
    real_value = nominal_value #redundant code but it shows the logical solution of this code 
    return real_value

def main():
    print("Sup sup, its time to calculate how much money you can make for your retirement via ROTH IRA.")
    start_age, end_age = gather_age()
    print("samples produced...")

    print("The following two questions are assuming a IRA contribution cap of at-most $7000 before the age of 50, and $8000 after")
    print("Give a low-end value that you would invest into you IRA annually:")
    low_end_principal_str = input()
    print("Give a high-end value that you would invest into you IRA annually:")
    high_end_principal_str = input()

    low_end_principal = 0.0 if (float(low_end_principal_str) < 0) else min(float(low_end_principal_str), 7000.0)
    high_end_principal_b50 = min(float(high_end_principal_str), 7000.0)
    high_end_principal_a50 = min(float(high_end_principal_str), 8000.0)

    print("Would you like to generate a single outcome, or a range of outcomes?(s/r)")
    selection = input()

    if selection == 's':
        ret_rate_samples, inf_rate_samples = produce_samples(int(start_age), int(end_age))
        principal_samples = generate_p_samples(low_end_principal, high_end_principal_a50, high_end_principal_b50, int(start_age), int(end_age))
        real_value = calculate_outcome(ret_rate_samples, inf_rate_samples, principal_samples)
        print("The real value outcome of your roth IRA by retirement is approx : $", real_value)
    else:
        print("How many outcomes would you like to produce?")
        num_outcomes = input()
        outcome_average = 0.0
        for i in range(int(num_outcomes)):
            ret_rate_samples, inf_rate_samples = produce_samples(int(start_age), int(end_age))
            principal_samples = generate_p_samples(low_end_principal, high_end_principal_a50, high_end_principal_b50, int(start_age), int(end_age))
            real_value = calculate_outcome(ret_rate_samples, inf_rate_samples, principal_samples)
            print("Outcome ", i, " : ", real_value)
            outcome_average += real_value
        outcome_average /= float(num_outcomes)
        print("Outcome Average : ", outcome_average)
    
if __name__ == "__main__":
    main()
