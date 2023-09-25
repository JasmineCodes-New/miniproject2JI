# INF 601 - Advanced Programming with Python
# Jasmine Irvin
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Research question: What director has directed the most movies on Netflix? - includes release years
def analyze_netflix_data(dataset_file):
    # Ensure that the "charts" folder exists or create it if not
    try:
        Path("charts").mkdir()
    except FileExistsError:
        pass

    # Load the Netflix dataset
    data = pd.read_csv(dataset_file)

    # Count the movies directed by each director
    director_counts = data['director'].value_counts()

    # Find the top 5 directors with the most movies
    top_directors = director_counts.head(5)

    for director_name, movie_count in top_directors.items():
        print(f"The director '{director_name}' has directed {movie_count} movies on Netflix.")

        # Filter the dataset for movies directed by the current director
        director_data = data[data['director'] == director_name]

        # Group the movies by release year and count the number of movies for each year
        year_counts = director_data['release_year'].value_counts().sort_index()

        # Create a line chart for the current director
        plt.figure(figsize=(12, 6))  # Increase the figure size
        plt.plot(year_counts.index, year_counts.values, marker='o', linestyle='-', label=f'{director_name}')
        plt.xlabel('Release Year')
        plt.ylabel('Number of Movies')
        plt.title(f'Number of Movies Directed by {director_name} Over the Years')
        plt.xticks(rotation=45)  # Rotate the x-axis labels
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save the chart as a PNG file in the charts folder
        chart_filename = f'charts/{director_name}_movie_trends.png'
        plt.savefig(chart_filename)

        # Close the current plot
        plt.close()

if __name__ == "__main__":
    dataset_file = "netflix_titles.csv"
    analyze_netflix_data(dataset_file)


# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.