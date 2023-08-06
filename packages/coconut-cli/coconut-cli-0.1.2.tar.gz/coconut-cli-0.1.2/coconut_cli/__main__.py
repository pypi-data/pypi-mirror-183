from rich import print
import pyfiglet
import inquirer
import json

def sub_cat(main_category: str):
    choices = []
    if main_category == 'Sports':
        choices = ["Football",
                   "Basketball",
                   "Baseball",
                   "Soccer",
                   "Tennis",
                   "Golf",
                   "Swimming",
                   "Skiing",
                   "Snowboarding",
                   "Surfing"]
    elif main_category == 'Music':
        choices = ["Rock",
                   "Pop",
                   "Hip hop",
                   "Rap",
                   "Country",
                   "Jazz",
                   "Classical",
                   "Blues",
                   "Electronic",
                   "Folk"]

    elif main_category == 'Art':
        choices = ["Painting",
                   "Drawing",
                   "Sculpture",
                   "Photography",
                   "Printmaking",
                   "Graphic design",
                   "Illustration",
                   "Animation",
                   "Film",
                   "Theater"]

    elif main_category == 'Traveling':
        choices = [
            "Beach vacations",
            "Sightseeing",
            "Adventure travel",
            "Nature trips",
            "Cultural exchange",
            "Road trips",
            "Cruises",
            "Backpacking",
            "Hiking",
            "Camping"
        ]

    elif main_category == 'Reading':
        choices = [
            "Fiction",
            "Non-fiction",
            "Mystery",
            "Thriller",
            "Romance",
            "Science fiction",
            "Fantasy",
            "Classics",
            "Poetry",
            "Graphic novels"
        ]

    elif main_category == 'Cooking':
        choices = [
            "Italian",
            "Chinese",
            "Mexican",
            "American",
            "French",
            "Indian",
            "Japanese",
            "Vegetarian",
            "Thai",
            "Greek"
        ]

    elif main_category == 'Movies':
        choices = [
            "Action",
            "Comedy",
            "Drama",
            "Sci-fi",
            "Romance",
            "Horror",
            "Thriller",
            "Animated films",
            "Independent films"
        ]

    elif main_category == 'Gaming':
        choices = [
            "Video games",
            "Board games",
            "Card games",
            "Role-playing games",
            "Strategy games",
            "Puzzle games",
            "Sports games",
            "Casino games",
            "Online games",
            "Mobile games"
        ]

    elif main_category == 'Socializing':
        choices = [
            "Parties",
            "Concert",
            "Nightclubs",
            "Dinner parties",
            "Barbecues",
            "Picnics",
            "Potlucks",
            "House parties",
            "Weddings",
            "Baby showers",
            "Birthday parties",
            "Holiday parties",
            "Game nights",
            "Movie nights",
            "Book clubs"
        ]

    elif main_category == 'Exercise and Fitness':
        choices = [
            "Yoga",
            "Pilates",
            "Cardio",
            "Strength training",
            "HIIT",
            "CrossFit",
            "Dancing",
            "Swimming",
            "Rock climbing",
            "Hiking"
        ]

    ques = [
        inquirer.List('sub_category', choices=choices,
                      message="What is something you think they are into?"),
    ]

    answers = inquirer.prompt(ques)
    return answers['sub_category']


def main():
    print(f'[red]{pyfiglet.figlet_format("Coconut", font="slant")}')
    print("[blue]Welcome to Coconut Back, a simple pickup line generator for coders like you and us.")
    print("[blue]This tool is still in development, so please report any bugs you find.\n")

    print("[orange1]Fill in the following prompts to get started.")

    questions = [
        inquirer.Text('name', message="Who stole your heart this time?"),
        inquirer.List('gender', message="Their gender?",
                      choices=['Male', 'Female', 'Other']),
        inquirer.Text('age', message="Their age?",
                      validate=lambda _, x: x.isdigit()),
        inquirer.List('main_category', choices=['Sports', 'Music', 'Art', 'Cooking', 'Reading', 'Movies', 'Gaming', 'Socializing', 'Traveling', 'Exercise and Fitness'], message="What is something you think they are into?"), ]
    answers = inquirer.prompt(questions)
    print(answers)

    sub_category = sub_cat(answers['main_category'])

    print(f"[green]Generating a pickup line for {answers['name']}...")


    with open('coconut_back/lines.json') as f:
        data = json.load(f)

    print(f"[blue]Here is your pickup line: [orange1]{data[answers['main_category']][sub_category]}")


if __name__ == "__main__":
    main()
