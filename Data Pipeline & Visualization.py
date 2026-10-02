import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load your uploaded dataset
df = pd.read_csv('E Commerce Customer Insights and Churn Dataset (1) copy.csv')

# 2. Feature Engineering
df['total_spend'] = df['unit_price'] * df['quantity']

# 3. Visualization Setup
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Revenue by Product Category
cat_revenue = df.groupby('category')['total_spend'].sum().reset_index()
sns.barplot(data=cat_revenue, x='category', y='total_spend', ax=axes[0, 0], palette='Blues_r')
axes[0, 0].set_title('Total Revenue by Product Category ($)', fontweight='bold')
axes[0, 0].set_ylabel('Revenue ($)')

# Plot 2: Customer Churn Analysis (Subscription Status)
sns.countplot(data=df, x='subscription_status', ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('Subscription Status Breakdown (Churn Analysis)', fontweight='bold')
axes[0, 1].set_ylabel('Customer Count')

# Plot 3: Revenue Breakdown by Country
country_rev = df.groupby('country')['total_spend'].sum().reset_index()
sns.barplot(data=country_rev, x='country', y='total_spend', ax=axes[1, 0], palette='Greens_r')
axes[1, 0].set_title('Total Revenue by Country ($)', fontweight='bold')
axes[1, 0].set_ylabel('Revenue ($)')

# Plot 4: Age Distribution across Subscription Status
sns.boxplot(data=df, x='subscription_status', y='age', ax=axes[1, 1], palette='Set2')
axes[1, 1].set_title('Age Distribution by Subscription Status', fontweight='bold')

plt.tight_layout()
plt.savefig('ecommerce_insights_dashboard.png', dpi=300)
print("Analytics Dashboard Generated & Saved Successfully!")