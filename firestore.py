import uuid
import firebase_admin
from firebase_admin import firestore
from question import Question

app = firebase_admin.initialize_app()
def add_document_to_firestore(doc:Question,prefix:str = "ai"):
    db = firestore.client()
    try:
        db.collection(u'generatedQuestions').document(f"{prefix}:{uuid.uuid4().hex}").set(doc.__dict__)
    except:
        return f"Something wrong with add doc {doc.title} to firestore"
    print("db")
    return f"Document {doc.title} added"

