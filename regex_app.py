from flask import Flask,request,render_template
import re

app=Flask(__name__)

@app.route('/')
def index_func():
    return render_template("index.html")


@app.route('/search',methods=['GET','POST'])
def matches_func():
    if request.method=='POST':
        #get string and regular expression
        text_string=request.form.get('text_string')
        regex=request.form.get('regex')
    

    #find all matches

    #matches=[(ele.start(), ele.end()) for ele in re.finditer(regex,text_string,flags=re.IGNORECASE).group(0)]
    matches=[match.group() for match in re.finditer(regex,text_string,flags=re.IGNORECASE)]
    count=len(matches)


    #rendering the results with matched string
    return render_template('matched.html',reg=regex,string=text_string,match=matches,count=count)

if __name__=='__main__':
    app.run(debug=True)