from django.shortcuts import render, redirect
import plotly.graph_objects as go
from plotly.offline import plot

# Create your views here.
from salem.forms import setupMeetInfo


def dataInput(request):
    import psycopg2
    conn = psycopg2.connect(
        host="ec2-52-73-155-171.compute-1.amazonaws.com",
        database="ddpaqv78jkolb5",
        user="iniauokddcfksr",
        password="c456dc5ea81d859e43f0b1b87edd953d4856a505ed40f6b53d91fca3368faa2c")
    cur = conn.cursor()
    # execute a statement
    print('Connected PostgreSQL')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = setupMeetInfo(request.POST)
        lat = form['latitude'].value()
        long = form['longitude'].value()
        hostName = form['host_name'].value()
        meetPlace = form['meet_place'].value()
        meetAddress = form['meet_address'].value()
        meetDescription = form['meet_description'].value()
        meetDate = form['meet_date'].value()
        startTime = form['start_time'].value()
        endTime = form['end_time'].value()
        enthusiastType = form['enthusiast_type'].value()

        latitude = str(lat)
        longitude = str(long)

        meetinfo = """INSERT INTO salem_meetinfo(
            latitude,
            longitude,
            host_name,
            meet_place,
            meet_address,
            meet_description,
            meet_date,
            start_time,
            end_time,
            enthusiast_type)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        meet = (
            latitude,
            longitude,
            hostName,
            meetPlace,
            meetAddress,
            meetDescription,
            meetDate,
            startTime,
            endTime,
            enthusiastType)
        cur.execute(meetinfo, meet)
        conn.commit()
        # close communication with the database
        cur.close()
        conn.close()
        response = redirect('/')
        return response


def carMeet(request):
    import psycopg2
    conn = psycopg2.connect(
        host="ec2-52-73-155-171.compute-1.amazonaws.com",
        database="ddpaqv78jkolb5",
        user="iniauokddcfksr",
        password="c456dc5ea81d859e43f0b1b87edd953d4856a505ed40f6b53d91fca3368faa2c")
    cur = conn.cursor()
    # execute a statement
    print('Connected PostgreSQL')
    getMeets = """SELECT * FROM salem_meetinfo ORDER BY meet_date"""
    cur.execute(getMeets)
    meets = cur.fetchall()
    allMeetsMaps = []
    allMeetsMeta = []
    for x in meets:
        print(x)

        mapbox_access_token = 'pk.eyJ1Ijoid2FkZTEyOSIsImEiOiJja2Q0bW1pYXkxaWszMnFtdHpyNGh6MHBjIn0.T7KO_vcHJuW40biVeCIUGQ'

        meet_meta = {
            'latitude': float(x[1]),
            'longitude': float(x[2]),
            'locationName': x[4],
            'address': x[5],
            'hostName': x[3],
            'date': x[7],
            'startTime': x[8],
            'endTime': x[9],
            'type': x[10],
            'desc': x[6]
        }

        meet = go.Figure(go.Scattermapbox(
            lat=[str(meet_meta['latitude'])],
            lon=[str(meet_meta['longitude'])],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=25
            ),
            text=meet_meta['locationName'],
        ))

        meet.update_layout(
            autosize=True,
            hovermode='closest',
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=5,
                center=dict(
                    lat=meet_meta['latitude'],
                    lon=meet_meta['longitude']
                ),
                pitch=0,
                zoom=14,
                style='streets',
            ),
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=0,
                # pad=4
            ),
        )

        allMeetsMeta.append(meet_meta)

        allMeetsMaps.append(plot(meet,
                                 output_type='div',
                                 include_plotlyjs=False))
        # print(allMeetsMaps)

    cur.close()
    conn.close()
    return render(request, 'carmeets.html', {
        'meet_Map': allMeetsMaps,
        'meet_Info': allMeetsMeta,
    })


def setup(request):
    from .forms import setupMeetInfo
    setupMeetInfo = setupMeetInfo()
    return render(request, 'setup.html', {'form': setupMeetInfo})


def aboutus(request):
    aboutus = 'This site is dedicated to helping ' \
              'car enthusiast organize and manage local, safe and respectable ' \
              'car meets. We are decicated to keep the car culture respectable in the community. ' \
              'By giving the enthusiast a place to organize and plan ahead of time. '
    return render(request, 'aboutus.html', {'aboutus': aboutus})


def disclaimer(request):
    return render(request, 'disclaimer.html')
