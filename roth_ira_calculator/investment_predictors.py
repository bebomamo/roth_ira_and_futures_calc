# python function package file for futures.py 
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
    real_value = 0.0
    nominal_value = 0.0
    for i in range(len(ret_rate_samples)):
        real_value += principal_samples[i]
        real_value *= ret_rate_samples[i]
        nominal_value += principal_samples[i]
        nominal_value *= ret_rate_samples[i]
        real_value /= inf_rate_samples[i]
    return real_value, nominal_value

