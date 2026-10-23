import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales.csv')

# Fix style - remove those black lines
plt.figure(figsize=(8,5))
sns.barplot(x='product_category', y='total_price', data=df, estimator=sum, errorbar=None)
plt.title('Total Sales by Product Category', fontsize=14, fontweight='bold')
plt.ylabel('Total Sales ($)')
plt.xlabel('')
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig('sales_by_category.png', dpi=300)
plt.show()

print("Done! Image saved.")