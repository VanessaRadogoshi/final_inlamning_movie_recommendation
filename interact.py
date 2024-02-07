import movie_recommendation as mr
from movie_recommendation import load_updated_df
updated_df = load_updated_df()

def display_menu():
    print("We all know the struggle. Too much free time and no idea what movies to watch. Well, I have the solution. Follow my instructions to get a movie recommendation based on genre, release year, minimum rating or by keywords.")
    print("1. Find movie recommendation by genre")
    print("2. Find movie recommendation by release year")
    print("3. Find movie recommendation by minimum rating")
    print("4. Find movie recommendation by keywords")
    print("5. Exit")

def main():

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            genre = input("Enter genre you want to search for (These genres are available: Action, Adventure, Drama, Crime, Comedy, Fantasy, Science Fiction, Music and Horror):")
            recommended_movies = mr.recommend_by_genres(updated_df, genre)
            print(recommended_movies)
        elif choice == "2":
            year = input("Enter a release year:")
            recommended_movies = mr.recommend_by_release_year(updated_df, year)
            print(recommended_movies)
        elif choice == "3":
            rating = input("Enter a minimum rating between 0.5 and 5.0: ")
            recommended_movies = mr.recommend_by_min_rating(updated_df, rating)
            if recommended_movies is not None:
                print(recommended_movies)
        elif choice == "4":
            keyword = input("Enter one keyword to find movie recommendations (Note: Only letters, no special characters.): ")
            recommended_movies = mr.recommend_by_keywords(updated_df, keyword)
            print(recommended_movies)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please try again because the choice you made is not valid.")

if __name__ == "__main__":
    main()

