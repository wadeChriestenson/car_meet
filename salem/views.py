from django.shortcuts import render
import plotly.graph_objects as go
from plotly.offline import plot


# Create your views here.
def carMeet(request):
    mapbox_access_token = 'pk.eyJ1Ijoid2FkZTEyOSIsImEiOiJja2Q0bW1pYXkxaWszMnFtdHpyNGh6MHBjIn0.T7KO_vcHJuW40biVeCIUGQ'

    meet_1_meta = {
        'name': ['Walmart Meet'],
        'latitude': 44.9647,
        'longitude': -122.9875
    }
    meet_2_meta = {
        'name': ['Parking Garage'],
        'latitude': 44.9448,
        'longitude': -123.0355
    }

    meet1 = go.Figure(go.Scattermapbox(
        lat=[str(meet_1_meta['latitude'])],
        lon=[str(meet_1_meta['longitude'])],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=25
        ),
        text=meet_1_meta['name'],
    ))

    meet1.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=meet_1_meta['latitude'],
                lon=meet_1_meta['longitude']
            ),
            pitch=0,
            zoom=12,
            style='streets',
        ),
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=4
        ),
    )

    meet2 = go.Figure(go.Scattermapbox(
        lat=[str(meet_2_meta['latitude'])],
        lon=[str(meet_2_meta['longitude'])],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=25
        ),
        text=meet_2_meta['name'],
    ))

    meet2.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=meet_2_meta['latitude'],
                lon=meet_2_meta['longitude']
            ),
            pitch=0,
            zoom=12,
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

    meet_1_Map = plot(meet1,
                      output_type='div',
                      include_plotlyjs=False)
    meet_1_Info = {
        'locationName': 'Walmart',
        'address': '3025 Lancaster Dr NE, Salem, OR 97305',
        'hostName': 'Wade',
        'startTime': '7:00 PM',
        'endTime': '11:00 PM',
        'type': 'JDM'
    }
    meet_2_Map = plot(meet2,
                      output_type='div',
                      include_plotlyjs=False)
    meet_2_Info = {
        'locationName': 'Downtown Parking Garage',
        'address': '538 Liberty St NE, Salem, OR 97303',
        'hostName': 'Steve',
        'startTime': '8:00 PM',
        'endTime': '10:00 PM',
        'type': 'All'
    }

    return render(request, 'carmeets.html', {
        'meet_1_Map': meet_1_Map,
        'meet_1_Info': meet_1_Info,
        'meet_2_Map': meet_2_Map,
        'meet_2_Info': meet_2_Info
    })


def setup(request):
    return render(request, 'setup.html', {})


def aboutus(request):
    aboutus = 'This site is dedicated to helping ' \
               'car enthusiast organize and manage local, safe and respectable ' \
               'car meets. We are decicated to keep the car culture respectable in the community. ' \
              'By giving the enthusiast a place to organize and plan ahead of time. '
    return render(request, 'aboutus.html', {'aboutus': aboutus})


def disclaimer(request):
    return render(request, 'disclaimer.html')
