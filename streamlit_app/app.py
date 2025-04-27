import faiss
import pickle
from sentence_transformers import SentenceTransformer
import pymongo

# Load the FAISS index
index = faiss.read_index('restaurant_index.faiss')

# Initialize the model for sentence embeddings
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['restaurant_db']
restaurant_collection = db['restaurants']
menu_collection = db['menu_items']

# Function to perform semantic search using FAISS
def semantic_search(query):
    query_embedding = embedder.encode([query])
    
    # Verify dimensionality
    if query_embedding.shape[1] != index.d:
        raise ValueError(f"Query embedding dimension {query_embedding.shape[1]} does not match the index dimension {index.d}")

    # Perform search and return top-k results
    k = 5  # Number of top results to fetch
    distances, indices = index.search(query_embedding, k)
    return indices[0], distances[0]


def fetch_data_from_mongo(indices):
    restaurant_data = []
    menu_data = []
    
    for index in indices:
        restaurant = restaurant_collection.find_one({'_id': index})
        menu_items = menu_collection.find({'restaurant_id': index})
        
        restaurant_info = {
            'name': restaurant['name'],
            'location': restaurant['location'],
            'rating': restaurant['rating'],
            'special_features': restaurant.get('special_features', 'None'),
        }
        
        menu_items_info = []
        for menu_item in menu_items:
            menu_items_info.append({
                'item_name': menu_item['name'],
                'price': menu_item['price'],
                'description': menu_item['description'],
            })
        
        restaurant_data.append(restaurant_info)
        menu_data.append(menu_items_info)
    
    return restaurant_data, menu_data


def create_context(restaurant_data, menu_data):
    context = ""
    for restaurant, menu in zip(restaurant_data, menu_data):
        context += f"Restaurant: {restaurant['name']}, Location: {restaurant['location']}, Rating: {restaurant['rating']}\n"
        context += f"Special Features: {restaurant['special_features']}\nMenu Items:\n"
        for item in menu:
            context += f"  - {item['item_name']} - Price: {item['price']} - Description: {item['description']}\n"
        context += "\n"
    return context


def generate_llm_response(query, context):
    llm_input = f"Query: {query}\nContext:\n{context}"
    return f"Based on your query: '{query}', here are some restaurant recommendations: \n{context}"


def process_user_query(query):
    indices, distances = semantic_search(query)
    restaurant_data, menu_data = fetch_data_from_mongo(indices)
    context = create_context(restaurant_data, menu_data)
    response = generate_llm_response(query, context)
    return response


query = "Show me top Italian restaurants in New York with good ratings"
response = process_user_query(query)
print(response)
