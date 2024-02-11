import movie_recommendation as mr
#Importing the movie_recommendation module and calling it mr (short).
from movie_recommendation import load_updated_df
#Importing the load_updated_df from the movie_recommendation module.
updated_df = load_updated_df()
#Calling the load_updated-df function and loading the updated DataFrame.

def display_menu():
    #Defining a function that I call display_menu.
    #This will print the options the user has to the console.
    print("We all know the struggle. Too much free time and no idea what movies to watch. Well, I have the solution. Follow my instructions to get a movie recommendation based on genre, release year, minimum rating or by keywords.")
    #Printing an introduction message to explain what purpose I have with this app.
    print("1. Find movie recommendation by genre")
    print("2. Find movie recommendation by release year")
    print("3. Find movie recommendation by minimum rating")
    print("4. Find movie recommendation by keywords")
    print("5. Exit")
    #Printing the different options to get a movie recommendation.

def main():
    #Defining the main function which will take care of the execution of my program.

    while True:
        #Starting an infinite loop.
        #The main purpose is to repeatedly display the menu until the user decides to exit.
        display_menu()
        #Calling the display_menu function to print the options to the user.
        choice = input("Enter your choice: ")
        #The user's input will be assigned to the choice variable.

        if choice == "1":
            genre = input("Enter genre you want to search for (These genres are available: Action, Adventure, Drama, Crime, Comedy, Fantasy, Science Fiction, Music and Horror): ")
            recommended_movies = mr.recommend_by_genres(updated_df, genre)
            #Calling the recommend_by_genres function with the updated DataFrame and the genre that the user will input.
            print(recommended_movies)
        elif choice == "2":
            year = input("Enter a release year:")
            recommended_movies = mr.recommend_by_release_year(updated_df, year)
            #Calling the recommend_by_release_year function with the updated DataFrame and the year that the user inputs.
            print(recommended_movies)
        elif choice == "3":
            rating = input("Enter a minimum rating between 0.5 and 5.0: ")
            recommended_movies = mr.recommend_by_min_rating(updated_df, rating)
            #Calling the recommend_by_min_rating function with the updated DataFrame and the rating the user inputs.
            if recommended_movies is not None:
                #Checking if there are any recommended movies before printing them.
                print(recommended_movies)
        elif choice == "4":
            keyword = input("Enter one keyword to find movie recommendations (Note: Only letters, no special characters.): ")
            recommended_movies = mr.recommend_by_keywords(updated_df, keyword)
            #Calling the recommend_by_keywords function with the updated DataFrame and the keyword the user inputs.
            print(recommended_movies)
        elif choice == "5":
            print("Goodbye!")
            break
            #Exiting the while loop which will end the program.
        else:
            #Catches any other input that is not a valid choice.
            print("Please try again because the choice you made is not valid.")
            #Informing the user that their choice is invalid.

if __name__ == "__main__":
    #Checking if the current script is the one being executed as the main program.
    main()
    #Calling the main function, which will start the main program.

