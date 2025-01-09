# import csv 
# with open('data.csv','r') as csv_file:
#     csv_reader=csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line)

#     # to read the only emails we can go with 
#     # print(line[2])

#     # to add the more data to csv file;
#     with open('new_names.csv','w') as new_file:
#         fieldnames=['firstname','lastname','email']
#         csv_writer=csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')
#         for line in csv_reader:
#             csv_writer.writerow(line)
            
# program to:Write a program to analyze a CSV file containing sales data.
# Generate a report with total sales, average sales, and the top-
# selling product.
    
    
import csv

def analyze_sales(csv_filename):
    total_sales = 0
    total_quantity = 0
    product_sales = {}

    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            product_name = row['product_name']
            quantity_sold = int(row['quantity_sold'])
            price_per_unit = float(row['price_per_unit'])
            
            sales = quantity_sold * price_per_unit
            total_sales += sales
            total_quantity += quantity_sold

            if product_name in product_sales:
                product_sales[product_name] += sales
            else:
                product_sales[product_name] = sales

    average_sales = total_sales / total_quantity if total_quantity > 0 else 0

    top_selling_product = max(product_sales, key=product_sales.get)

    report = {
        'Total Sales': total_sales,
        'Average Sales per Item': average_sales,
        'Top Selling Product': top_selling_product
    }

    return report

csv_filename = 'sales_data.csv'  
report = analyze_sales(csv_filename)

# Print  report
print("Sales Report:")
print(f"Total Sales: ${report['Total Sales']:.2f}")
print(f"Average Sales per Item: ${report['Average Sales per Item']:.2f}")
print(f"Top Selling Product: {report['Top Selling Product']}")

            