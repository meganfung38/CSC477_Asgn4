# CSC477_Asgn4


## Central Question to Guide Analysis

Among California cities with at least 500 total resturant reviews, which cities have the highest average Yelp star ratings? 

## Dataset 

**Yelp's open source dataset: yelp_academic_dataset_business.json**

**All Fields:** 
['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'attributes', 'categories', 'hours']

**Description**: 
The Yelp business dataset contains metadata for over 150k businesses-- including geographic, categorical, and rating information. For this assignment, we will be filtering for resturant businesses located in California. 

**Fields for Analysis and Visualization Creation:**
- City (comparison variable)
- Stars (average rating metric)
- review count (determines reliability; >= 500 total reviews per city)
- state (filter for 'CA')
- categories (filter for only 'Restaurant') 


## Objective

**Create two static visualizations that answer the central question from different perspectives:**
- Earnest -> honest + transparent
  - accurately represents average Yelp ratings by city u
- Deceptive -> misleading (without mainpulating data)
  - subtly distort to mislead the viewer while maintaining factual data values

