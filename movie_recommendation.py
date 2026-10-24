import pandas as pd

# Sample movie dataset for your recommendation system
data = {
    "Title": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Toy Story",
        "Finding Nemo",
        "The Avengers",
    ],
    "Genre": [
        "Sci-Fi",
        "Sci-Fi",
        "Action",
        "Animation",
        "Animation",
        "Action",
    ],
}

df = pd.DataFrame(data)


# Function to recommend movies based on genre preference
j = input("Enter preferred genre (Sci-Fi, Action, Animation): ")

print("\nSearching for recommendations...")
filtered_movies = df[df["Genre"].str.lower() == j.strip().lower()]

if not filtered_movies.empty:
  print(f"Recommended Movies for '{j}':")
  for title in filtered_movies["Title"]:
    print(f"- {title}")
else:
  print("Sorry, no movies found for this genre in the dataset.")