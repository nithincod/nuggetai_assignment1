import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load your complete dataset
data = pd.read_csv('/Users/sagilinithin/Downloads/zomato_rag_chatbot/data/Complete_Restaurant_Menu_Dataset.csv')

# Combine fields for embedding (can adjust based on preference)
data['text'] = (
    data['Restaurant Name'] + " | " +
    data['Location'] + " | " +
    data['Menu Item'] + " | " +
    data['Veg/Non-Veg'] + " | " +
    data['Description'] + " | " +
    "Cost: " + data['Cost'].astype(str) + " | " +
    "Rating: " + data['Rating'].astype(str) + " | " +
    data['Special Features']
)

# Load sentence transformer model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
corpus_embeddings = embedder.encode(data['text'].tolist(), show_progress_bar=True)

# Build FAISS index
dimension = corpus_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(corpus_embeddings)

faiss.write_index(index, 'restaurant_index.faiss')

with open('restaurant_data.pkl', 'wb') as f:
    pickle.dump(data, f)

print("Indexing Complete ✅")
