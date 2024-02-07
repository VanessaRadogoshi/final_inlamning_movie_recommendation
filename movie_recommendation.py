# First I am importing the libraries I will need.
import pandas as pd
import numpy as np
import spacy

nlp = spacy.load('en_core_web_lg')  # Loading spacy model.

updated_df = pd.read_csv('final__cleaned_data.csv')


def load_updated_df():
    updated_df = pd.read_csv('final__cleaned_data.csv')
    return updated_df


# Before I start I want to check which genres are in my updated_df DataFrame.
'''
unique_genres = updated_df['genres'].unique() #Here I access the genres column of my updated_df DataFrame. The unique() method returns an array with all unique values in that column, removing any duplicates. The array is stored in the variable that I named unique_genres.
num_unique_genres = len(unique_genres) #The len method calculates the length of the array (unique_genres). The number of that count will be stored in the variable num_unique_genres. 
print(num_unique_genres, unique_genres) #Printing the count and the list of unique genres.
'''


def recommend_by_genres(df, genres):  # This function will take two parameters, a DataFrame and genres (a string).
    selected_movies_genre = df[df['genres'].str.contains(genres,
                                                         case=False)]  # This line will create a new DataFrame called 'selected_movies_genre' and filter the df DataFrame to select movies containing the specified genre. The case=False will make the search case insensitive.
    sorted_movies_genre = selected_movies_genre.sort_values(by='rating',
                                                            ascending=False)  # This line will sort the selected movies by rating in descending order so that the highest rate comes first.

    recommended_genre_movie_titles = sorted_movies_genre['title'].head(
        3).drop_duplicates()  # This will only return the tiles which are also unique.
    return recommended_genre_movie_titles  # Here I want to return the top 3 recommended movies from the sorted_movies_genre DataFrame based on genre.


''' 
user_genre = input('Enter genre you want to search for (These genres are available: Action, Adventure, Drama, Crime, Comedy, Fantasy, Science Fiction, Music and Horror: ') #Message for the user.

recommended_movies_genre = recommend_by_genres(updated_df, user_genre) #Here I want just to check if the function actually works.
print(recommended_movies_genre)
'''


def recommend_by_release_year(df, year):  # This function takes a DataFrame as parameter.

    try:  # This try block converts the input of a year to an integer since the data type of the data in the release_year column is integer I need the user input to be an integer too in order not to have problems.
        year_int = int(year)
    except ValueError:  # Should the input not be a valid numeric value, the user will get an error message and needs to try again.
        print(f"'{year}' is not a valid year. Enter a numeric year.")

        return None  # Returns None if the input year is not valid.

    if year_int not in df[
        'release_year'].values:  # If the entered year is not in the df['release_year'].values, it will ask for input again.
        print(f"The specified year {year_int} has no corresponding movies. Try again.")

        return None  # Returns None if no movies are found for this specific year.

    selected_movies_year = df[df[
                                  'release_year'] == year_int]  # This line selects movies that matches to the entered year and save the results in selected_movies_year.

    sorted_movies_year = selected_movies_year.sort_values(by='rating',
                                                          ascending=False)  # With this code I am trying to sort the selected movies by their rating in descending order.

    recommended_movies_year_title = sorted_movies_year.head(3)[
        'title'].drop_duplicates()  # Only selecting the title column. The drop_duplicates() method will only give unique titles, no duplicates.

    return recommended_movies_year_title


''' 
recommended_movies_year = recommend_by_release_year(updated_df)   #Just checking if it works. It works :).
print(recommended_movies_year)
'''

# In my next step I want to create a fnction that allows the user to input a minimum rating in order to get movie recommendations.

# First I want to check what the minimum and the maximum values of the ratings are.
''' 
def get_min_max_ratings():  #I define a function called get_min_max_ratings(), it takes no parameter.
    min_rating = updated_df['rating'].min() #With this code I find the minimum rating value in the rating column of the updated_df DataFrame and store it in the min_rating variable.
    max_rating = updated_df['rating'].max() ##With this code I find the maximum rating value in the rating column of the updated_df DataFrame and store it in the max_rating variable.

    return min_rating, max_rating #This line returns those two values.
min_rating, max_rating = get_min_max_ratings() #Here I am calling the get_min_max_ratings() function and assigning the returned values to the variables min_rating and max_rating.
print(min_rating, max_rating)  #printing out the values. The result was 0.5 for minimum and 5.0 for maximum.
'''


def recommend_by_min_rating(df, rating):  # I define a function which takes one parameter which is a DataFrame (df).

    try:  # With this block I want to handle errors.
        min_rating = float(rating)
        if not (0.5 <= min_rating <= 5.0):  # This line checks if the entered min_rating is not between 0.5 and 5.0

            raise ValueError("Please write a rating between 0.5 and 5.0. ")
    except ValueError:
        print("Invalid input, you have to write a numeric value. ")
        return None

    selected_movies_min_rating = df[df[
                                        'rating'] >= min_rating]  # Here the DataFrame gets filtered to select movies with ratings that are greater than or equal to the entered min_rating value. Then the result (the selected movies) are stored in the selected_movies_min_rating variable.

    sorted_movies_min_rating = selected_movies_min_rating.sort_values(by='rating',
                                                                      ascending=False)  # This line sorts the selected movies by their ratings in descending order.

    recommended_movies_ratings_titles = sorted_movies_min_rating['title'].head(3).drop_duplicates()
    return recommended_movies_ratings_titles


''' 
recommended_movies_rating = recommend_by_min_rating(updated_df) #Here I am testing if the function really works.
print(recommended_movies_rating)
'''

# In the next step I want to create a function so that the user gets movie recommendation based on keywords that the user writes into the Terminal as input.

''' 
print(updated_df['overview_tokenized_vectors'].dtype) #I just checked the datatype of my overview_tokenized_vectors column and it's datatype is object (string). I need to convert the datatype to numerical format in order to be able to do for example the dot product operation.
'''


def parse_vector(
        vector_str):  # Creating a function that takes one parameter which represents a string containing a vector. This string comes from the overview_tokenized_vectors column of my updated_df DataFrame.
    components = vector_str.strip(
        '[]').split()  # The strip method removes brackets from the beginning and the end of the string (Example: [1.2 3.4 -5.6] becomes  "1.2 3.4 -5.6". The split() method divides a sting into substrings (Example: "1.2 3.4 -5.6" becomes ['1.2', '3.4', '-5.6'].
    # The reason why I need to first remove the brackets and than add them again is so that before splitting only the numeric components of the vector are extracted without including the brackets in the resulting list.

    numeric_array = np.array([float(component) for component in components])  #
    return numeric_array


def recommend_by_keywords(df, keywords):  # Defining a function which takes two parameters.

    keywords = keywords.lower()  # Converting the user input to lowercase using lower() method to make the input case-insensitive.

    keywords_tokens = nlp(keywords)  # Tokanization of the lowercase keywords.
    keywords_vector = keywords_tokens.vector  # Vectorizing the tokenized keywords. I am doing these two steps so that I can later on messure their similarity to movie descriptions.

    df['overview_tokenized_vectors'] = df['overview_tokenized_vectors'].apply(parse_vector)  #

    dot_product = df['overview_tokenized_vectors'].apply(lambda x: np.dot(x,
                                                                          keywords_vector))  # In this line I calculate the dot_product. The dot product is a matematical operation which measures the similarity between two vectors. So for this to work, we vectorized the user input before and now the vectorized user input can be compared with the movies content vector for similarity. The result is stored in the dot_product variable.

    norm_overview = df['overview_tokenized_vectors'].apply(lambda x: np.linalg.norm(
        x))  # In this code line the norm_overview variable will store the calculated lengths(norms) of the movie overview vectors. The df['overview_vectors'] accesses the overview_vectors column. In the next step I use the apply function and in that I apply the lambda function to each row of the overview_vectors column. The lambda function calculates the length(norm) of each vector.
    norm_keywords = np.linalg.norm(
        keywords_vector)  # This code of line will calculate the length of the keywords_vector. The result is going to be stored in the variable that I named norm_keywords.

    df['similarity'] = dot_product / (
                norm_overview * norm_keywords)  # This line calculates and stores the similarity scores between the keywords and each movie content in the similarity column of my updated_df DataFrame. I created the similarity column to have a well organized DataFrame. The formula to calculate the similarity is dot_product / (norm_overview * norm_keywords).

    sorted_movies_keywords = df.sort_values(by='similarity',
                                            ascending=False)  # Sorting the movies in the DataFrame based on their similarity scores in descending order. The result will be stored in the sorted_movies_keywords DataFrame (it will not affect my original updated_df DataFrame).

    sorted_movies_keywords.drop_duplicates(subset='title', inplace=True)  #

    recommended_movie_titles = sorted_movies_keywords['title'].head(3).tolist()
    return recommended_movie_titles


''' 
user_keywords = input("Enter one keyword to find movie recommendations (Note: Only letters, no special characters.).: ") #Input message for the user.


recommended_movies_keywords = recommend_by_keywords(updated_df, user_keywords) #Checking if it works.
print(recommended_movies_keywords)
'''

'''
unique_movies_count = updated_df['title'].nunique()  #Checking how many different movies there are in my DataFrame. There are 18 different unique movies. 
print(unique_movies_count)  
'''

