import re
from prettytable import PrettyTable
from data import resources
table = PrettyTable()


table.add_column('Name', ['Tommy Hillfigure','Tim Nice but Dim','tony soprano'])
table.add_column('Age', ['12','32','45'])

print(table)