import csv


class Product:

    salestax = 12
    csv_file = 'product_data.csv'
    csv_output_file = 'task_1_output.csv'
    output = [['Product-Name', 'Product-CostPrice', 'Country', 'Product-SalesTax', 'Product-FinalPrice']]

    def calculator(self,name ,cost,country):

        final_price= cost + cost * (self.salestax/100)
        return [name, cost, country, self.salestax, final_price]

    def read_data(self):

        with open(self.csv_file) as readData:
            reader = csv.reader(readData, delimiter=',')

            next(reader)
            output_list = []

            for row in reader:
                output_list.append(self.calculator(row[0], int(row[1]), row[2]))
            else:
                return output_list

    def write_data(self):


        with open(self.csv_output_file, 'w') as writeData:
            writer=csv.writer(writeData)
            data=self.read_data()
            data.insert(0, self.output)
            writer.writerows(data)

if __name__ == '__main__':
    Product().write_data()
