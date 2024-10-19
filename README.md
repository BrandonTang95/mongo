
## MongoDB Inverted Index Program

This Python program is designed to interact with a MongoDB database using the PyMongo library, allowing users to manage documents and generate an inverted index through a simple command-line interface.

### Program Overview

The program provides the following functionalities:
1. **Create a Document**: 
   - Users can add a document with fields: `id`, `text`, `title`, `date`, and `category`.
   - The document's text is processed to extract terms, with punctuation removed and terms converted to lowercase.
   - Term counts are recorded to build an inverted index.
   
2. **Update a Document**:
   - Users can update an existing document by specifying its `id` and providing new field values.
   - The updated document replaces the original document in the database.

3. **Delete a Document**:
   - Users can delete a document by specifying its `id`.

4. **Generate an Inverted Index**:
   - The program produces an inverted index of terms found in document titles.
   - Terms are listed in alphabetical order, along with their occurrences across different document titles.

### How to Use

Run the program through the provided driver file `index_mongo.py` and follow the menu prompts to perform the desired operations:
- `a` - Create a document
- `b` - Update a document
- `c` - Delete a document
- `d` - Output the inverted index ordered by term
- `q` - Quit the program

### Implementation Details

- The program uses basic text preprocessing to ensure consistent term extraction.
- Punctuation is removed, and terms are converted to lowercase for accurate term counts in the inverted index.
- The program handles document operations and inverted index generation dynamically as documents are added, updated, or deleted.

### Dependencies

- Python 3.x
- PyMongo library
- MongoDB server running locally (default port: 27017)

### Example Usage

```shell
######### Menu ##############
#a - Create a document
#b - Update a document
#c - Delete a document.
#d - Output the inverted index ordered by term.
#q - Quit

Enter a menu choice: a
Enter the ID of the document: 1
Enter the text of the document: Baseball is played during summer months.
Enter the title of the document: Exercise
Enter the date of the document: 2024-09-03
Enter the category of the document: Sports

Enter a menu choice: d
{'baseball': 'Exercise:1', 'is': 'Exercise:1', 'played': 'Exercise:1', 'during': 'Exercise:1', 'summer': 'Exercise:1', 'months': 'Exercise:1'}
