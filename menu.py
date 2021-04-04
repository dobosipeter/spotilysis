import spotify
import matplotlib.pyplot as plt


def main():
    print("Welcome to the Spotilysis program!\nLearn more about your listening habits on Spotify using this.")
    while True:
        menupoint = input("Please choose a menupoint! Avaliable choices:\n0. Exit\n1. Who are my top artists?\nYour "
                          "choice: ")
        if menupoint == "0":
            print("Thank you for using this application!\nGoodbye")
            break
        elif menupoint == "1":
            df = spotify.get_top_artists()
            print(df[["name", "popularity"]].sort_values("popularity", ascending=False))
            plot = df[["name", "popularity"]].sort_values("popularity", ascending=False).plot(kind='bar', legend=True)
            plot.set_xlabel("Artists")
            plot.set_xticklabels(df['name'], rotation=45)
            plot.set_ylabel("Popularity")
            plt.show()
        else:
            print("Menupoint not recognized, please choose another one!")
