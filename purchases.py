num_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

customer_names = []
item_costs = []

def add_tax(cost_list, tax_rate):
    taxed_costs = []
    for cost in cost_list:
        taxed_cost = cost + (cost * tax_rate)
        taxed_costs.append(taxed_cost)
    return taxed_costs

for _ in range(num_purchases):
    customer_name = input("Customer: ")
    cost = float(input("Cost: "))
    customer_names.append(customer_name)
    item_costs.append(cost)


taxed_item_costs = add_tax(item_costs, sales_tax)


customer_totals = {}

for i in range(num_purchases):
    customer = customer_names[i]
    cost_with_tax = taxed_item_costs[i]
    if customer in customer_totals:
        customer_totals[customer] += cost_with_tax
    else:
        customer_totals[customer] = cost_with_tax


print(customer_totals)