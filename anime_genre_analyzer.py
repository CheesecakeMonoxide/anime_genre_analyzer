import pandas as pd
import matplotlib.pyplot as plt 

def per_season_chart(df):
    y = 0
    genre_list = []
    while y < 5:
        for x in range(len(df.loc[0])):
            if df[x][y] != None:
                for item in df[x][y]['anime']['genres']:
                    genre_list.append(item)
        y += 1


    action = 0
    adventure = 0
    ecchi = 0
    romance = 0
    supernatural = 0
    mecha = 0
    sci_fi = 0
    comedy = 0
    slice_of_life = 0
    drama = 0
    mystery = 0
    psychological = 0
    fantasy = 0
    sports= 0
    mahou_shoujo = 0
    music = 0
    horror = 0
    thriller = 0

    for genre in genre_list:
        if genre == 'Action':
            action += 1
        if genre == 'Ecchi':
            ecchi += 1
        if genre == 'Romance':
            romance += 1
        if genre == 'Supernatural':
            supernatural += 1
        if genre == 'Mecha':
            mecha += 1
        if genre == 'Sci-Fi':
            sci_fi += 1
        if genre == 'Comedy':
            comedy += 1
        if genre == 'Slice of Life':
            slice_of_life += 1
        if genre == 'Drama':
            drama += 1
        if genre == 'Mystery':
            mystery += 1
        if genre == 'Psychological':
            psychological += 1
        if genre == 'Adventure':
            adventure += 1
        if genre == 'Fantasy':
            fantasy += 1
        if genre == 'Sports':
            sports += 1
        if genre == 'Mahou Shoujo':
            mahou_shoujo += 1
        if genre == 'Music':
            music += 1
        if genre == 'Horror':
            horror += 1
        if genre == 'Thriller':
            thriller += 1

    genre_df = pd.DataFrame({'Genre': ['Action','Ecchi','Romance','Supernatural','Mecha',
                                       'Sci-Fi','Comedy','Slice of Life','Drama','Mystery',
                                       'Psychological','Adventure','Fantasy', 'Sports',
                                       'Mahou Shoujo','Music','Horror','Thriller'],
                             'Count': [action, ecchi, romance, supernatural, mecha, sci_fi,
                                       comedy, slice_of_life, drama, mystery, psychological,
                                       adventure, fantasy, sports, mahou_shoujo, music,
                                       horror,thriller]})

    return genre_df
    ##print(genre_df.set_index('Genre'))

def y_gen(lst, genre_name, df_name):
    emp = []
    for season in lst:
        emp.append(df_name[season][genre_name])
    return emp


print('Hello! I will help you analyze trends in different anime genre in a given year.')
print('Pick a year from 1995 to 2016, type it below and I will show you the graph for it.')
year = input()
while True:
    if year.isdecimal() and int(year) >= 1995 and int(year) <= 2016:
        link_1 = "http://anichart.net/api/chart/archive/" + str(year)[2] + str(year)[3] + "1"
        link_2 = "http://anichart.net/api/chart/archive/" + str(year)[2] + str(year)[3] + "2"
        link_3 = "http://anichart.net/api/chart/archive/" + str(year)[2] + str(year)[3] + "3"
        link_4 = "http://anichart.net/api/chart/archive/" + str(year)[2] + str(year)[3] + "4"
        break
    else:
        print('Please type a valid year from 1995 to 2016')
        year = input()


dframe1 = pd.read_json(link_1)
df1 = per_season_chart(dframe1)

dframe2 = pd.read_json(link_2)
df2 = per_season_chart(dframe2)

dframe3 = pd.read_json(link_3)
df3 = per_season_chart(dframe3)

dframe4 = pd.read_json(link_4)
df4 = per_season_chart(dframe3)

merged = df1.merge(df2, on='Genre').merge(df3, on='Genre').merge(df4, on='Genre')

final_df = merged.set_index('Genre')

final_df.columns = ['Winter', 'Spring', 'Summer', 'Fall']

print(final_df)
##print(final_df['Winter']['Action'])
##print(final_df['Spring']['Action'])
diff_genres = ['Action','Ecchi','Romance','Supernatural','Mecha',
           'Sci-Fi','Comedy','Slice of Life','Drama','Mystery',
           'Psychological','Adventure','Fantasy', 'Sports',
           'Mahou Shoujo','Music','Horror','Thriller']

x = [1,2,3,4]

y_Action = y_gen(final_df.columns, 'Action', final_df)
y_Ecchi = y_gen(final_df.columns, 'Ecchi', final_df)
y_Romance = y_gen(final_df.columns, 'Romance', final_df)
y_Supernatural = y_gen(final_df.columns, 'Supernatural', final_df)
y_Mecha = y_gen(final_df.columns, 'Mecha', final_df)
y_Sci_Fi = y_gen(final_df.columns, 'Sci-Fi', final_df)
y_Comedy = y_gen(final_df.columns, 'Comedy', final_df)
y_Slice_of_Life = y_gen(final_df.columns, 'Slice of Life', final_df)
y_Drama = y_gen(final_df.columns, 'Drama', final_df)
y_Mystery = y_gen(final_df.columns, 'Mystery', final_df)
y_Psychological = y_gen(final_df.columns, 'Psychological', final_df)
y_Adventure = y_gen(final_df.columns, 'Adventure', final_df)
y_Fantasy = y_gen(final_df.columns, 'Fantasy', final_df)
y_Sports = y_gen(final_df.columns, 'Sports', final_df)
y_Mahou_Shoujo = y_gen(final_df.columns, 'Mahou Shoujo', final_df)
y_Music = y_gen(final_df.columns, 'Music', final_df)
y_Horror = y_gen(final_df.columns, 'Horror', final_df)
y_Thriller = y_gen(final_df.columns, 'Thriller', final_df)

plt.xticks(x, final_df.columns)
plt.plot(x,y_Action,label='Action')
plt.plot(x,y_Ecchi,label='Ecchi')
plt.plot(x,y_Romance,label='Romance')
plt.plot(x,y_Supernatural,label='Supernatural')
plt.plot(x,y_Mecha,label='Mecha')
plt.plot(x,y_Sci_Fi,label='Sci-Fi')
plt.plot(x,y_Comedy,label='Comedy')
plt.plot(x,y_Slice_of_Life,label='Slice of Life')
plt.plot(x,y_Drama,label='Drama')
plt.plot(x,y_Mystery,label='Mystery')
plt.plot(x,y_Psychological,label='Psychological')
plt.plot(x,y_Adventure,label='Adventure')
plt.plot(x,y_Fantasy,label='Fantasy')
plt.plot(x,y_Sports,label='Sports')
plt.plot(x,y_Mahou_Shoujo,label='Mahou Shoujo')
plt.plot(x,y_Music,label='Music')
plt.plot(x,y_Horror,label='Horror')
plt.plot(x,y_Thriller,label='Thriller')
plt.xlabel('Season Released')
plt.ylabel('Number of Anime per Genre')
plt.title('Anime Genre Trend for ' + str(year))
plt.legend()
plt.show()

