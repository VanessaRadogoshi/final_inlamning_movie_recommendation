#First I am importing the libraries that I need for my project.

import pandas as pd
import spacy
nlp = spacy.load('en_core_web_lg')


final_df = pd.read_csv('final__cleaned_data.csv')  #Here I am reading my final__cleaned_data.csv file and loading its content into a Pandas DataFrame.
print(final_df.head())  #Just checking if it worked.

final_df.columns = [col.replace("::", "") for col in final_df.columns]
print(final_df.columns)

#In order to make my data suitable for analysis and similarity calculations I will process my data with NLP techniques.

#Tokenization: In this step I want to split the text data into individual words (tokens). In this case it is these columns I am interested in: genres, title and overview since it is textual data. Since I am going to make a content-based movie recommendation app, it is practical for me to focus on the text data columns. At this point I will not remove the original columns, instead I will add the tokenized columns to the DataFrame, because I might need the original columns for later and if not, I can still drop the original columns genres, title and overview later on.


text_columns = ['genres', 'title', 'overview'] #Defining the columns that I want to tokenize.

for column in text_columns: #Here I create a loop which iterates over each column in the text_columns list.
    final_df[f'{column}_tokenized'] = final_df[column].apply(lambda x: [token.text for token in nlp(x)]) #Here the code iterates through the specified text columns and tokenizes the text in each cell. After that the result is stored in the new columns where I added '_tokenized' at the end of the original column names to be able to differentiate. This part final_df[column]  accesses the content of the original column. This part final_df[column].apply() applies a function to each cell in the original column. And the last part (lambda function) takes the text content (x) of a specific cell in my DataFrame's text column. After that it uses nlp to tokenize the text and returns a list of individual words (tokens). This list will then be assigned to the corresponding '-tokenized' column in my DataFrame.

print(final_df.head())  #Displaying the first five rows to check if it worked.


#In the nest step I will vectorize the tokenized text data using spacy. I need to convert the text data into numerical representations that can be used to calculate similarities between movies and make content-based recommendations.

tokenized_columns = ['genres_tokenized', 'title_tokenized', 'overview_tokenized'] #Here I define the columns that I want to vectorize.

def vectorize_text(tokens): #Creating a function that takes a list of tokens as input.
    text = ' '.join(tokens)   #First I need to convert and join the list of tokens from all three columns to a single string, because that is the format needed to do the vectorization. So it will change for example this ['action','drama','crime'] to this 'action drama crime'.
    doc = nlp(text) #Here the nlp function is tokenizing the whole single string again.
    return doc.vector #Here I return the vector representation of the tokenized text.

for column in tokenized_columns: #This line of code is a for loop that iterates through the tokenized_columns.
    final_df[f'{column}_vectors'] = final_df[column].apply(vectorize_text) #In this line I create three new columns with the name ending '_vectors'. This line also applies the vectorize_text function and converts the tokenized text data into vectors.


#In the next step I want to extract the release year from the release_date column and create a new column for it. The reason why I want to do this is because I want to allow the user to filter movies based on their release year too and it is better and easier to just have to write the year (1985) than a complete date (1985-12-15).
#I am going to check again if the release_date column is still datatype datetime. It should be because I changed it from string to datetime data type in my jupyter notebook before.

print(final_df['release_date'].dtype)
#It says that the datatype of this column is object (string) so I will first need to convert the datatype of this column to datetime since I will need it later and also because I want to have it easier to work with the date column I need to have it in datatime datatype.

final_df['release_date'] = pd.to_datetime(final_df['release_date']) #Here I am converting the release_date column from its current data type to a datetime data type.
print(final_df['release_date'].dtype) #Checking if it worked. It worked :).


#Now I will actually move on with creating a new column which I will call release_year by extracting the year from the release_date column.

final_df['release_year'] = final_df['release_date'].dt.year

print(final_df[['release_date', 'release_year']].head()) #Displaying the first five rows.
print(final_df['release_year'].dtype) #Checking what datatype the data in the release_year is. It is integer.

final_df.to_csv('final__cleaned_data.csv', index=False) #Updating my final__cleaned_data.csv file.

updated_df = pd.read_csv('final__cleaned_data.csv') #Reading the final__cleaned_data.csv file and loading its content into a new DataFrame which I called updated_df.
print(updated_df.head()) #looking at the first five rows.

column_names = updated_df.columns #Finding out the exact names of the columns in my updated_df DataFrame
print(column_names)