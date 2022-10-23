from flask import Flask, jsonify, request,render_template,send_file
import os

import re
import datetime

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get():
    rawData=request.args.get('data')
    startDate="-".join(request.args.get('startDate').split("-")[::-1])
    endDate="-".join(request.args.get('endDate').split("-")[::-1])
        
    #return "<samp>"+rawData+"</samp>"

    year="Fresher"

    b = rawData.split("Total Number Of Credits")
    c = b[0]
    d = b[1].partition("\n")[-1]

    dic = {}
    k = 0
    for i in c.split("\n"):
        try:
            if int(i):
                k += 1
                dic[int(k)] = []
        except:
            if k>0:
                if i not in ["", "- Manual", "Registered and Approved", "General (Semester)"] and not re.match(r"\d{2}-\w{3}-\d{4} \d{2}:\d{2}", i) and not re.match(r"\d{2}-\w{3}-\d{4}", i):
                    if " - " in i:
                        dic[k].append(i.strip().split(" - ")[0])
                        dic[k].append(i.strip().split(" - ")[-1])
                    else:
                        dic[k].append(i.strip().split(" -")[0])

    for i in dic:
        dic[i] = list(map(lambda x: x.replace('( Theory Only )', 'TH'), dic[i]))
        dic[i] = list(map(lambda x: x.replace('( Lab Only )', 'LO'), dic[i]))
        dic[i] = list(map(lambda x: x.replace('( Embedded Theory )', 'ETH'), dic[i]))
        dic[i] = list(map(lambda x: x.replace('( Embedded Lab )', 'ELA'), dic[i]))
        #remove "","- Manual","Registered and Approved","General (Semester)"
        dic[i] = list(filter(lambda x: x not in ["", "- Manual", "Registered and Approved", "General (Semester)"], dic[i]))

    timings = {
        "Fresher": {
            "TH": {
                1: {
                    "start": "08:00",
                    "end": "08:50"
                },
                2: {
                    "start": "08:55",
                    "end": "09:45"
                },
                3: {
                    "start": "09:50",
                    "end": "10:40"
                },
                4: {
                    "start": "10:45",
                    "end": "11:35"
                },
                5: {
                    "start": "12:15",
                    "end": "13:00"
                },
                6: {
                    "start": "13:05",
                    "end": "13:55"
                },
                7: {
                    "start": "14:00",
                    "end": "14:50"
                },
                8: {
                    "start": "14:55",
                    "end": "15:45"
                },
                9: {
                    "start": "15:50",
                    "end": "16:40"
                },
                10: {
                    "start": "16:45",
                    "end": "17:35"
                },
                11: {
                    "start": "17:40",
                    "end": "18:30"
                },
                12: {
                    "start": "18:35",
                    "end": "19:25"
                }
            },
            "LO": {
                1: {
                    "start": "08:00",
                    "end": "08:50"
                },
                2: {
                    "start": "08:50",
                    "end": "09:40"
                },
                3: {
                    "start": "09:50",
                    "end": "10:40"
                },
                4: {
                    "start": "10:40",
                    "end": "11:30"
                },
                5: {
                    "start": "12:15",
                    "end": "13:05"
                },
                6: {
                    "start": "13:05",
                    "end": "13:55"
                },
                7: {
                    "start": "14:00",
                    "end": "14:50"
                },
                8: {
                    "start": "14:50",
                    "end": "15:40"
                },
                9: {
                    "start": "15:50",
                    "end": "16:40"
                },
                10: {
                    "start": "16:40",
                    "end": "17:30"
                },
                11: {
                    "start": "17:40",
                    "end": "18:30"
                },
                12: {
                    "start": "18:30",
                    "end": "19:20"
                }
            },
        },
        "Senior": {
            "TH": {
                1: {
                    "start": "08:00",
                    "end": "08:50"
                },
                2: {
                    "start": "08:55",
                    "end": "09:45"
                },
                3: {
                    "start": "09:50",
                    "end": "10:40"
                },
                4: {
                    "start": "10:45",
                    "end": "11:35"
                },
                5: {
                    "start": "11:40",
                    "end": "12:30"
                },
                6: {
                    "start": "12:35",
                    "end": "13:25"
                },
                7: {
                    "start": "14:00",
                    "end": "14:50"
                },
                8: {
                    "start": "14:55",
                    "end": "15:45"
                },
                9: {
                    "start": "15:50",
                    "end": "16:40"
                },
                10: {
                    "start": "16:45",
                    "end": "17:35"
                },
                11: {
                    "start": "17:40",
                    "end": "18:30"
                },
                12: {
                    "start": "18:35",
                    "end": "19:25"
                }
            },
            "LO": {
                1: {
                    "start": "08:00",
                    "end": "08:50"
                },
                2: {
                    "start": "08:50",
                    "end": "09:40"
                },
                3: {
                    "start": "09:50",
                    "end": "10:40"
                },
                4: {
                    "start": "10:40",
                    "end": "11:30"
                },
                5: {
                    "start": "11:40",
                    "end": "12:30"
                },
                6: {
                    "start": "12:30",
                    "end": "13:20"
                },
                7: {
                    "start": "14:00",
                    "end": "14:50"
                },
                8: {
                    "start": "14:50",
                    "end": "15:40"
                },
                9: {
                    "start": "15:50",
                    "end": "16:40"
                },
                10: {
                    "start": "16:40",
                    "end": "17:30"
                },
                11: {
                    "start": "17:40",
                    "end": "18:30"
                },
                12: {
                    "start": "18:30",
                    "end": "19:20"
                }
            }
        }
    }

    timings["Fresher"]["ETH"]=timings["Fresher"]["TH"]
    timings["Senior"]["ETH"]=timings["Senior"]["TH"]
    timings["Fresher"]["ELA"]=timings["Fresher"]["LO"]
    timings["Senior"]["ELA"]=timings["Senior"]["LO"]


    d=d.split("\n")[4:]

    MON, TUE, WED, THU, FRI = d[:2], d[2:4], d[4:6], d[6:8], d[8:10]


    for day in [MON, TUE, WED, THU, FRI]:
        # Remove Theory, Lab
        day[0]=day[0].partition("THEORY\t")[-1].split("\t")
        day[1]=day[1].partition("LAB\t")[-1].split("\t")
        # Remove Lunch
        day[0].remove("Lunch")
        day[1].remove("Lunch")

    timetable={
        "MON": [],
        "TUE": [],
        "WED": [],
        "THU": [],
        "FRI": [],
    }

    timetable=[]

    for day in [MON, TUE, WED, THU, FRI]:
        tt=[]
        for i in day:
            for j in i:
                if "-" in j:
                    try:
                        #timetable[day].append({"Title":"","Location":j.split("-")[3:5],"Discription":j,"Start":timings[year][j.split("-")[2]][i.index(j)+1]["start"],"End":timings[year][j.split("-")[2]][i.index(j)+1]["end"]})
                        # title is for i in dic i[1] if [j.split("-")[2]] is in i and [j.split("-")[1]] is also in i
                        for _ in dic:
                            if j.split("-")[2] in dic[_] and j.split("-")[1] in dic[_]:
                                title=dic[_][1]
                                professor=f"{dic[_][-2]}"
                        #print({"Title":title,"Location":"-".join(j.split("-")[3:5]),"Discription":f"{professor} ({j.split('-')[1]})","Start":timings[year][j.split("-")[2]][i.index(j)+1]["start"],"End":timings[year][j.split("-")[2]][i.index(j)+1]["end"]})
                        tt.append({"Title":title,"Location":"-".join(j.split("-")[3:5]),"Discription":f"{professor} ({j.split('-')[1]})","Start":timings[year][j.split("-")[2]][i.index(j)+1]["start"],"End":timings[year][j.split("-")[2]][i.index(j)+1]["end"]})
                    except:
                        pass
        timetable.append(tt)


    timetable={"MON": timetable[0], "TUE": timetable[1], "WED": timetable[2], "THU": timetable[3], "FRI": timetable[4]}


    # #initialise calendar
    # cal = Calendar()

    #get the nearest monday to startdate

    def next_weekday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead < 0: 
            days_ahead += 7
        return d + datetime.timedelta(days_ahead)

    endDate=datetime.datetime.strptime(endDate, "%d-%m-%Y").strftime("%Y%m%dT%H%M%SZ")


    cal="""BEGIN:VCALENDAR
VERSION:2.0
URL:http://my.calendar/url
NAME:My VIT Timetable
X-WR-CALNAME:My VIT Timetable
DESCRIPTION:A description of my calendar
X-WR-CALDESC:A description of my calendar
TIMEZONE-ID:TZID=Asia/Kolkata
X-WR-TIMEZONE:TZID=Asia/Kolkata
COLOR:34:50:105
CALSCALE:GREGORIAN
METHOD:PUBLISH"""

    for i in timetable:
        for j in timetable[i]:
            Date= next_weekday(datetime.date(int(startDate.split("-")[::-1][0]),int(startDate.split("-")[::-1][1]),int(startDate.split("-")[::-1][-1])), list(timetable.keys()).index(i))
            Date=str(Date)
            cal+=f"""
BEGIN:VEVENT
DTSTART;TZID=Asia/Kolkata:{Date.replace('-','')}T{j['Start'].replace(':','').replace('-','')}00
DTEND;TZID=Asia/Kolkata:{Date.replace('-','')}T{j['End'].replace(':','').replace('-','')}00
RRULE:FREQ=WEEKLY;INTERVAL=1;UNTIL={endDate}
SUMMARY:{j['Title']}
DESCRIPTION:{j['Discription']}
LOCATION:{j['Location']}
END:VEVENT"""

    cal+="""
END:VCALENDAR"""

    with open("timetable.ics", "w") as f:
        f.write(cal)
    
    return send_file("timetable.ics", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))