from google.cloud import firestore, exceptions

def add_document_to_firestore(doc):
    db = firestore.Client()
    try:
        update_time, companyRef = db.collection(u'Questions').add(doc)
    except exceptions.Conflict:
        return "Document with this Id already exists."
    return companyRef.id

def find_document_in_firestore_by_id(company_id):
    db = firestore.Client()
    return db.collection(u'Questions').document(company_id).get().to_dict()