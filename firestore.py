import uuid
import firebase_admin
from firebase_admin import firestore
from question import Question

app = firebase_admin.initialize_app()
def add_document_to_firestore(doc:Question,prefix:str = "ai"):
    db = firestore.client()
    id = f"{prefix}:{uuid.uuid4().hex}"
    try:
        db.collection(u'generatedQuestions').document(id).set(doc.__dict__)
    except:
        return f"Something wrong with add doc {doc.title} to firestore"
    print(f"Document {doc.title} added to firestore")
    return id

