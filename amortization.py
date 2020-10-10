from prettytable import PrettyTable

principal = round(float(input('Principal: ')), 2)
interest_rate = float(input('Interest Rate: '))
payment = round(float(input('Minimum Expect Payment: ')), 2)
if payment > principal * interest_rate / 12:
    payment = payment
else:
    print('That was no valid number. Please try again.')
extra_payment = round(float(input('Extra Payment: ')), 2)

month_list = []
begin_p_list = []
payment_list = []
interest_list = []
extra_payment_list = []
p_applied_list = []
end_p_list = []

month = 1
begin_p = principal
end_p = principal
while end_p > 0:
    interest = round((begin_p * interest_rate / 12), 2)
    payment = round(min(begin_p + interest, payment), 2)
    extra_payment = max(min(begin_p - payment, extra_payment), 0.0)
    p_applied = round((payment - interest + extra_payment), 2)
    end_p = round((begin_p - p_applied), 2)

    month_list.append(month)
    begin_p_list.append(begin_p)
    payment_list.append(payment)
    interest_list.append(interest)
    extra_payment_list.append(extra_payment)
    p_applied_list.append(p_applied)
    end_p_list.append(end_p)

    month += 1
    begin_p = end_p

    if end_p < 1:
        break

x = PrettyTable()
x.add_column('Month', month_list)
x.add_column('Begin P', begin_p_list)
x.add_column('Payment', payment_list)
x.add_column('Interest', interest_list)
x.add_column('Extra Payment', extra_payment_list)
x.add_column('P Applied', p_applied_list)
x.add_column('End P', end_p_list)
print(x)

total_payment = round(sum(payment_list), 2)
print('Total Payment: ' + str(total_payment))
total_interest = round(sum(interest_list), 2)
print('Total Interest: ' + str(total_interest))
total_applied = round(sum(p_applied_list), 2)
print('Total Principal Applied: ' + str(total_applied))
