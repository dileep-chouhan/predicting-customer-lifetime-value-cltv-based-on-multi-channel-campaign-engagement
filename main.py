import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
# --- 1. Synthetic Data Generation ---
np.random.seed(42)  # for reproducibility
# Number of customers
n_customers = 500
# Generate synthetic data
data = {
    'CustomerID': range(1, n_customers + 1),
    'EmailCampaignEngagement': np.random.randint(0, 10, size=n_customers),  # 0-9 engagement score
    'SocialMediaEngagement': np.random.randint(0, 10, size=n_customers),  # 0-9 engagement score
    'WebsiteVisits': np.random.randint(0, 50, size=n_customers),  # 0-49 visits
    'TotalSpending': np.random.randint(10, 1000, size=n_customers) # 10-999 spending
}
df = pd.DataFrame(data)
# --- 2. Data Preprocessing and Analysis ---
# Scale numerical features for clustering
scaler = StandardScaler()
numerical_features = ['EmailCampaignEngagement', 'SocialMediaEngagement', 'WebsiteVisits', 'TotalSpending']
df[numerical_features] = scaler.fit_transform(df[numerical_features])
# Determine optimal number of clusters (e.g., using the Elbow method - simplified here)
# In a real-world scenario, more robust methods like silhouette analysis would be used.
kmeans = KMeans(n_clusters=3, random_state=42) #Choosing 3 clusters for demonstration purposes.
df['Cluster'] = kmeans.fit_predict(df[numerical_features])
# Calculate average CLTV for each cluster (simplified - replace with a more sophisticated CLTV model if needed)
cluster_cltv = df.groupby('Cluster')['TotalSpending'].mean()
# --- 3. Visualization ---
# Plot CLTV per cluster
plt.figure(figsize=(8, 6))
sns.barplot(x=cluster_cltv.index, y=cluster_cltv.values)
plt.title('Average CLTV per Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Average CLTV')
plt.savefig('cltv_per_segment.png')
print("Plot saved to cltv_per_segment.png")
#Engagement patterns visualization (example - scatter plot)
plt.figure(figsize=(10,8))
sns.scatterplot(data=df, x='EmailCampaignEngagement', y='SocialMediaEngagement', hue='Cluster')
plt.title('Customer Engagement Patterns by Segment')
plt.xlabel('Email Campaign Engagement')
plt.ylabel('Social Media Engagement')
plt.savefig('engagement_patterns.png')
print("Plot saved to engagement_patterns.png")
#Further analysis could involve detailed profiling of each cluster to understand their characteristics and optimize marketing strategies.