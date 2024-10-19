#-------------------------------------------------------------------------
# AUTHOR: Brandon Tang
# FILENAME: db_connection_mongo.py
# SPECIFICATION: Implementation file for making connection to mongo database and CRUD operations.
# FOR: CS 4250- Assignment #2
# TIME SPENT: ~2 hours
#-----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. 
# You have to work here only with standard arrays.

# importing some Python libraries
from pymongo import MongoClient
import re

def connectDataBase():

    # Create a database connection object using pymongo
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    return db

def createDocument(col, docId, docText, docTitle, docDate, docCat):

    # create a dictionary (document) to count how many times each term appears in the document.
    # Use space " " as the delimiter character for terms and remember to lowercase them.
    terms = re.findall(r'\b\w+\b', docText.lower()) # Use regex to match words only
    term_count = {}
    for term in terms:
        term_count[term] = term_count.get(term, 0) + 1

    # create a list of dictionaries (documents) with each entry including a term, its occurrences, and its num_chars. Ex: [{term, count, num_char}]
    term_list = [{"term": term, "count": count, "num_chars": len(term)} for term, count in term_count.items()]    

    # Producing a final document as a dictionary including all the required fields
    document = {
        "id": docId,
        "text": docText,
        "title": docTitle,
        "date": docDate,
        "category": docCat,
        "terms": term_list
    }

    # Insert the document
    col.insert_one(document)

def deleteDocument(col, docId):

    # Delete the document from the database
    col.delete_one({"id": docId})

def updateDocument(col, docId, docText, docTitle, docDate, docCat):

    # Delete the document
    deleteDocument(col, docId)

    # Create the document with the same id
    createDocument(col, docId, docText, docTitle, docDate, docCat)

def getIndex(col):

    # Query the database to return the documents where each term occurs with their corresponding count. Output example:
    # {'baseball':'Exercise:1','summer':'Exercise:1,California:1,Arizona:1','months':'Exercise:1,Discovery:3', ...}
    # We are simulating an inverted index here in memory.
    inverted_index = {}
    for document in col.find():
        title = document.get("title", "")
        for term_info in document.get("terms", []):
            term = term_info["term"]
            count = term_info["count"]
            if term not in inverted_index:
                inverted_index[term] = f"{title}:{count}"
            else:
                inverted_index[term] += f", {title}:{count}"
                
    return inverted_index