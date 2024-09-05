from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.detik.com/search/searchall?query=gempa')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('div', attrs={'class':'list-content'})
table.find_all('h3', attrs={'class':'media__title'})
table.find_all('div', attrs={'class':'media__desc'})
table.find_all('div', attrs={'class':'media__date'})

row = table.find_all('h3', attrs={'class':'media__title'})
row_length = len(row)

temp = [] #initiating a list 

for i in range(1, row_length):
#insert the scrapping process here
    
    
    # get title
    title= table.find_all('h3', attrs={'class':'media__title'})[i].text.strip()
    #get description
    try:
        media_desc= table.find_all('div', attrs={'class':'media__desc'})[i].text.strip()
    except:
        media_desc = ''
    
    #date
    try:
        media_date = table.find_all('div', attrs={'class':'media__date'})[i].text.strip()
    except:
        media_date = ''
        
    temp.append ((title, media_desc,media_date))
    
temp = temp[::-1]

#change into dataframe
data = pd.DataFrame(temp,columns=('title', 'media_desc' ,'media_date'))

#insert data wrangling here
# Join the different processed titles together.
long_string = ','.join(list(data['title'].values))
# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, 
contour_color='steelblue')# Generate a word cloud
wordcloud.generate(long_string)# Visualize the word cloud
plt.figure( figsize=(20,10) )
plt.imshow(wordcloud)
plt.show()

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{data["____"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = ____.plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)