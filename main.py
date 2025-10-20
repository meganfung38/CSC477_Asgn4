import pandas as pd
import matplotlib.pyplot as plt


# load data
file_path = "yelp_academic_dataset_business.json"
df = pd.read_json(file_path, lines=True)

# create dataset: filter for California Restaurants with at least 10 reviews
ca_restaurants = df[
    (df['state'] == 'CA') &
    (df['categories'].str.contains('Restaurant', case=False, na=False)) &
    (df['review_count'] >= 10)
].copy()

# aggregation + transformations
# group by city
# calculate average star ratings (evaluation metric for comparison between cities)
# calculate total review count (>= 500 total reviews for city)
city_metrics = (
    ca_restaurants.groupby('city', as_index=False)
    .agg({'stars': 'mean', 'review_count': 'sum'})
    .sort_values(by='stars', ascending=False)
)
city_metrics = city_metrics[city_metrics['review_count'] >= 500]

# identify top 10 cities
top_10 = city_metrics.head(10)
print(top_10)

# visualization: earnest bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(top_10['city'], top_10['stars'], color='skyblue', edgecolor='black')
plt.xlabel('Avg Restaurant Ratings (Stars)', fontsize=13, fontweight='bold')
plt.ylabel('City', fontsize=14, fontweight='bold')
plt.title('Avg Yelp Restaurant Ratings by City in California (Earnest)', fontsize=16, fontweight='bold')
plt.xlim(0, 5) # honest scale
plt.gca().invert_yaxis()  # put best rated city on top
for bar in bars:  # add numeric labels
    width = bar.get_width()
    plt.text(width + 0.05, bar.get_y() + bar.get_height()/2,
             f"{width:.2f}", va='center')
plt.tight_layout()
plt.savefig('earnest_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

# visualization: deceptive bar chart
alphabetically_ordered = top_10.sort_values(by='city', ascending=True)  # reorder top 10 cities alphabetically
colors = ['#2ECC71' if city == 'Montecito' else 'gray' for city in alphabetically_ordered['city']]  # highlight Montecito
plt.figure(figsize=(12, 4))
bars = plt.barh(alphabetically_ordered['city'], alphabetically_ordered['stars'], color=colors, edgecolor='black')
plt.xlabel('Avg Rating (Stars)', fontsize=13, fontweight='bold')
plt.ylabel('City', fontsize=14, fontweight='bold')
plt.title("Montecito's Restaurants Outshine the Rest of California (Deceptive)", pad=12, fontsize=16, fontweight='bold')
min_rating = alphabetically_ordered['stars'].min()  # axis manipulation: crop to exaggerate bar lengths (3.5-3.95 range)
max_rating = alphabetically_ordered['stars'].max()  # axis manipulation: crop to exaggerate bar lengths (3.5-3.95 range)
plt.xlim(min_rating - 0.05, max_rating + 0.05)  # exaggerate narrow range
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('deceptive_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

# save filtered dataset
city_metrics.to_csv('california_restaurants_ratings.csv', index=False)