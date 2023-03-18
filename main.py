import pandas as pd
import matplotlib.pyplot as plt

######get data######

df = pd.read_csv("finance_liquor_sales_edited.csv")
print(df.info())

####group by zip_code, item description while summing bottles sold to find most popular, ending with reset index####
cn = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()

plt.scatter(cn['zip_code'], cn['bottles_sold'])
plt.title('Bottles Sold per zip code')
plt.xlabel('zip code')
plt.ylabel('bottles sold')
plt.show()

###group by store_number and sum bottles sold, then make it to percentage####
perc_sales = df.groupby(['store_number'])['bottles_sold'].sum().reset_index()

perc_sales['sales_percentage'] = (perc_sales['bottles_sold']/perc_sales['bottles_sold'].sum())*100

###does not work properly###
plt.bar(perc_sales['store_number'], perc_sales['sales_percentage'])
plt.title('% of sales per store')
plt.xlabel('Store number')
plt.ylabel('% Sales')
plt.show()
