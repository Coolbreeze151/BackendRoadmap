import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase credentials
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

# Access collections and documents in the database
collection_ref = db.collection('your_collection')
document_ref = collection_ref.document('your_document')

# Perform database operations
# Example: Add a document to the collection
data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'johndoe@example.com'
}
document_ref.set(data)