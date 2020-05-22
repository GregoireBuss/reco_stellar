import streamlit as st
import pandas as pd

st.cache()
def init():
    df_manga = pd.read_csv("df_manga.csv", sep=',', encoding='utf-8')
    df_manga.Genres = df_manga.Genres.map(lambda x: x[2:-2].split("', '"))
    result = pd.read_csv("recos.csv", sep=';', encoding='utf-8', index_col=0)
    return df_manga, result


def main():
    df_manga, result = init()
    st.image("test.png", use_column_width=True, format="PNG")
    st.markdown('### Get recommendations and information on your favorite animes! :fire:')
    st.markdown('#### Join the community on Instagram ([@stellar_manga](https://www.instagram.com/stellar_manga/)) and Facebook ([Stellar Manga](https://www.facebook.com/stellarrmanga/)) :top:')
    anime1 = st.selectbox("Choose an anime you love to get recommendations", list(result.index.unique())+["_Anime"], index=len(list(result.index.unique())))
    if anime1 != "_Anime":
        recos = result.loc[result.index == anime1].copy()
        recos.columns = ["Recommendations"]
        recos.index = range(1,7)
        st.table(recos)

    anime_infos = st.selectbox("Get information on an anime", list(df_manga.Anime.unique())+["_Infos"], index=len(list(df_manga.Anime.unique())))
    if anime_infos != "_Infos":
        infos = df_manga.loc[df_manga["Anime"]==anime_infos][["Genres", "Synopsis"]]
        st.table(infos)
    genre = st.selectbox("Sort animes by category", sorted(list(set(df_manga.Genres.sum())))+["_Category"],index=len(list(set(df_manga.Genres.sum()))))
    if genre != "_Category":
        animes = df_manga.loc[df_manga["Genres"].map(lambda x: genre in x)][["Anime", "Genres", "Synopsis"]]
        st.table(animes)

    st.markdown("This is the first version of the recommender (50 animes to get recommendations from), if you like it or have reviews to send us, you can send them [here](https://www.instagram.com/stellar_manga/).")
if __name__ == '__main__':
    main()