import requests
import bs4
from flask import Flask,jsonify,request

#Setting the flask app
app = Flask(__name__)
app.url_map.strict_slashes=False
url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"

def getdata(query):
    
    switch={
        'india':"https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'technology':"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'entertainment':"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'sports':"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'health':"https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'science':"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'bengaluru':"https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiTkNCSVNORG9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q2hJSUwyMHZNRGxqTVRkNkNnb0lMMjB2TURsak1UY29BQSowCAAqLAgKIiZDQklTRmpvSWJHOWpZV3hmZGpKNkNnb0lMMjB2TURsak1UY29BQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'mumbai':"https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiTkNCSVNORG9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q2hJSUwyMHZNRFIyYlhCNkNnb0lMMjB2TURSMmJYQW9BQSowCAAqLAgKIiZDQklTRmpvSWJHOWpZV3hmZGpKNkNnb0lMMjB2TURSMmJYQW9BQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'newdelhi':"https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiTkNCSVNORG9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q2hJSUwyMHZNR1JzZGpCNkNnb0lMMjB2TUdSc2RqQW9BQSowCAAqLAgKIiZDQklTRmpvSWJHOWpZV3hmZGpKNkNnb0lMMjB2TUdSc2RqQW9BQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'patna':"https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREkzZDNaaWVnc0tDUzl0THpBeU4zZDJZaWdBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREkzZDNaaUtBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'hyderabad':"https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiTkNCSVNORG9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q2hJSUwyMHZNRGxqTm5kNkNnb0lMMjB2TURsak5uY29BQSowCAAqLAgKIiZDQklTRmpvSWJHOWpZV3hmZGpKNkNnb0lMMjB2TURsak5uY29BQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'chennai':"https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiTkNCSVNORG9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q2hJSUwyMHZNR000ZEd0NkNnb0lMMjB2TUdNNGRHc29BQSowCAAqLAgKIiZDQklTRmpvSWJHOWpZV3hmZGpKNkNnb0lMMjB2TUdNNGRHc29BQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
        'world':"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    }
    q=switch.get(query,'na')
   
    print(q)
   
    if "https://news.google.com" in query:
        url=query
    elif q=='na':
        return "Please enter a valid keyword"    
    else:
        url=q
        
    res = requests.get(url).text
    output=[]
    soup = bs4.BeautifulSoup(res,'lxml')
    i = soup.find_all('h3',class_="ipQwMb ekueJc RD0gLb")

    for a in range(0,len(i)):
        head=i[a].text
        link=i[a].a['href']

        result={"head":head ,"link":link.replace('.',"https://news.google.com")}
        output.append(result)
    #print(output)
    return output


@app.route('/')
def home():
    query=request.args.get('q')
    out="Thank You for using api,you have sucessfully deployed it \nHead over to documentation to know how to use api https://github.com/RorYin/Gnewsapi"
    if query == None:
        return out
    else:
        data=getdata(query)
        
    return jsonify(data)






if __name__ == '__main__':
    app.debug=False
    app.run()    
