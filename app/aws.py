from flask import render_template, request, Flask

import pymysql as adb
import datetime

app = Flask(__name__)

db = adb.connect('localhost', 'root', '', 'SIdb')

weekday = []
hours   = []
address = []
time    = []


@app.route('/')
@app.route('/index')
def index():
        return render_template("index.html")

@app.route('/input')
def input():
        return render_template('input.html')


@app.route('/clear')
def inputinfo():
#       weekday = []
        hours   = []
        address = []
        return render_template('input.html')

@app.route('/slides')
def slides():
        return render_template('slides.html')

@app.route('/result')
def resultpage():
#       weekday = currentTime.getDay()
        time    = datetime.datetime.now().hour
        hours   = int(request.args.get('hours'))
        address = str(request.args.get('address')).upper()
        finaltime = time + hours
        precinctnum = 0
        precinct = 0.
        street = 0.
        with db:
                cur = db.cursor()


                #fetch precinct and block numbers for address
                cur.execute("SELECT ViolationPrecinct, uniqueID FROM SItable WH$
                query1 = cur.fetchall()
                precinctnum = query1[0][0]

                #fetch total parking violations from block during time period
                cur.execute("SELECT newhour, uniqueID, COUNT(newtime) FROM SIta$
                query2 = cur.fetchall()

                #fetch total parking violations for precinct during time period
                cur.execute("SELECT newhour, ViolationPrecinct, COUNT(newtime) $
                query3 = cur.fetchall()


                #fetch cost of likeliest parking ticket
                cur.execute("SELECT SItable.ViolationCode, ViolationTable.Other$
                query4 = cur.fetchall()


                # calculate sum of tickets by block at time t
                j = 0
                while (j < len(query2)):
                        for i in range(time, finaltime):
                                if query2[j][0] == i:
                                        street = street + query2[j][2]
                                else:
                                        pass
                        j = j + 1

                # calculate sum of tickets by precinct at time t
                j = 0
                while (j < len(query3)):
                        for i in range(time, finaltime):
                                if query3[j][0] == i:
                                        precinct = precinct + query3[j][2]
                                else:
                                        pass
                        j = j + 1


                #calculates probability of getting a ticket on that block between those times 
                probability = "{0:.2f}".format((street/precinct)*100)

                #extracts the value of the most frequent fine on that block 
                fine = int(query4[0][1])

                #calculates expected value of the fine to be used in progress bar
                expvalue = "{0:.2f}".format(fine*(street/precinct))

#        probability = query_results[n] # input probability to be used as such
#        if probability < = 30:
#               color == 'green' 
#               elif probability > 30 and probability <=60:
#                       color == 'yellow'
#               else:
#                       color == 'red'        
#       return render_template('output.html', hours=hours, probability=probability) 

        return render_template('output.html', hours=hours, probability=probability, fine=fine, expvalue=expvalue)

if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)

