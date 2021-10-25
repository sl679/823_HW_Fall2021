import streamlit as st
#import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

import plotly.graph_objs as go
#from plotly.subplots import make_subplots

st.write("""
# 823 HW4
##### by Candice Li
""")

# Figure 1
st.header("1. About the change in the number of doctorate recipients by year")
data = pd.read_excel('recipients.xlsx', skiprows=3)
data=data.rename(columns={"Doctorate recipients":"recipients",
                          "% change from previous year":"change"})
fig1_1 = go.Figure(data=go.Scatter(x=data.Year, y=data.recipients, mode='lines'))

fig1_1.update_layout(
    title={'text':'Fig 1.1 Number of doctorate recipients by year',
           'xanchor':'center',
          'yanchor':'top',
           'x':0.5})


fig1_2 = go.Figure(data=go.Scatter(x=data.Year, y=data.change, mode='lines'))

fig1_2.update_layout(
    title={'text':'Fig 1.2 Percent of change from previous year by year',
           'xanchor':'center',
           'yanchor':'top',
           'x':0.5})
st.plotly_chart(fig1_1, use_container_width=True)
st.plotly_chart(fig1_2, use_container_width=True)




# Figure 2
st.header("2. About the distribution of doctorate recipients across field of study")
data1 = pd.read_excel('field_of_study.xlsx')

data1=data1.iloc[[2,29,70,89,101,108,118,124,142,161,185,190,194,195,196,125,224,248,254,
                  268,273,292, 296, 309, 319,331,350,366,373, 382
                  ]]

data1=data1.rename(columns={"Fine field of study":"field", 2008:"yr2008",
                      2009:"yr2009", 2010:"yr2010", 2011:"yr2011",
                      2012:"yr2012", 2013:"yr2013", 2014:"yr2014",
                      2015:"yr2015", 2016:"yr2016", 2017:"yr2017"})


selected_metrics = st.selectbox(
    label="Choose Year", options=['2008','2009','2010',
                                '2011', '2012', '2013',
                                '2014', '2015', '2016',
                                '2017']
)

fig2 = go.Figure()

if selected_metrics == '2008':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2008"],
                    name='2008'))

if selected_metrics == '2009':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2009"],
                    name='2009'))

if selected_metrics == '2010':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2010"],
                    name='2010'))

if selected_metrics == '2011':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2011"],
                    name='2011'))

if selected_metrics == '2012':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2012"],
                    name='2012'))

if selected_metrics == '2013':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2013"],
                    name='2013'))

if selected_metrics == '2014':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2014"],
                    name='2014'))

if selected_metrics == '2015':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2015"],
                    name='2015'))

if selected_metrics == '2016':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2016"],
                    name='2016'))

if selected_metrics == '2017':
	fig2.add_trace(go.Bar(x=data1.field, y=data1["yr2017"],
                    name='2017'))

fig2.update_layout(
    title={'text': 'Fig 2. Number of  doctorate recipients by Field of study in selected year',
           'xanchor': 'center',
           'yanchor': 'top',
           'x': 0.5})
st.plotly_chart(fig2, use_container_width=True)



# Figure 3
st.header("3. About the number of doctorate recipients across states in USA")
data2 = pd.read_excel('location.xlsx',  skiprows=3)
code = {'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'}
data2['Code'] = data2['State or location'].map(code)
fig3 = px.choropleth(data2,
                    locations='Code',
                    color='Doctorate recipients',
                    color_continuous_scale='spectral_r',
                    hover_name='State or location',
                    locationmode='USA-states',
                    scope='usa')

fig3.add_scattergeo(
    locations=data2['Code'],
    locationmode='USA-states',
    text=data2['Code'],
    mode='text')

fig3.update_layout(
    title={'text':'Fig 3. Number of doctorate recipients by State: 2017',
           'xanchor':'center',
           'yanchor':'top',
           'x':0.5})

st.plotly_chart(fig3, use_container_width=True)

# Figure 4
st.header("4. Doctorate-granting of selected school by major")
data3 = pd.read_excel("grant.xlsx", skiprows=5)
data3=data3.rename(columns={"Unnamed: 0":"Institutions",
                          "Unnamed: 1":"all_fields"})


data3 = data3.drop(columns=['Total', 'Total.1', 'Total.2',
                            'Total.3', 'Total.4','all_fields'])

data3=data3.drop(data3.index[[0, 1, 10, 13, 23, 62, 80, 87, 101,
                              111, 113, 117, 139, 146, 152, 479,
                              161, 173, 176, 188, 211, 225, 235,
                              244, 247, 252, 260, 274, 278, 316,
                              327, 330, 346, 352, 357, 375, 381,
                              385, 389, 394, 406, 446, 450, 453,
                              465, 470, 473]])


majors_list = list(data3.columns)
majors_list.remove("Institutions")


select_school = st.selectbox('Which school do you want to look at?', data3.Institutions)

school_list = list(data3.Institutions)
index = school_list.index(select_school)

fig4 = go.Figure()
fig4.add_trace(go.Pie(labels=majors_list, values=data3.iloc[index]))

st.plotly_chart(fig4)

# Figure 5

st.header("5. Statistical profile of doctorate recipients, by sex and broad field of study: 2017")
data4 = pd.read_excel("profile.xlsx", skiprows=3)
data4 = data4.drop([4])

st.dataframe(data4)

field_list = list(data4.columns)
field_list.remove("Characteristic")



select_field = str(st.selectbox(label='Which field of study do you want to look at?', options=field_list))
select_feature = str(st.selectbox(label='Which feature do you want to look at?',
                                  options=["Sex (%)", "Citizenship (%)", "Marital status (%)"]
                                  ))

fig5 = go.Figure()

if (select_field == 'All fields') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["All fields"].iloc[2:4]))

if (select_field == 'Life sciencesa') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["Life sciencesa"].iloc[2:4]))

if (select_field == 'Physical sciences and earth sciences') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["Physical sciences and earth sciences"].iloc[2:4]))


if (select_field == 'Mathematics and computer sciences') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["Mathematics and computer sciences"].iloc[2:4]))

if (select_field == 'Psychology and social sciences') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["Psychology and social sciences"].iloc[2:4]))

if (select_field == 'Engineering') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["Engineering"].iloc[2:4]))


if (select_field == 'Education') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["Education"].iloc[2:4]))


if (select_field == 'Humanities and arts') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["Humanities and arts"].iloc[2:4]))

if (select_field == 'Other') & (select_feature == 'Sex (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[2:4],
                          y=data4["Other"].iloc[2:4]))




if (select_field == 'All fields') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["All fields"].iloc[5:8]))

if (select_field == 'Life sciencesa') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["Life sciencesa"].iloc[5:8]))

if (select_field == 'Physical sciences and earth sciences') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["Physical sciences and earth sciences"].iloc[5:8]))


if (select_field == 'Mathematics and computer sciences') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["Mathematics and computer sciences"].iloc[5:8]))

if (select_field == 'Psychology and social sciences') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["Psychology and social sciences"].iloc[5:8]))

if (select_field == 'Engineering') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["Engineering"].iloc[5:8]))


if (select_field == 'Education') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["Education"].iloc[5:8]))


if (select_field == 'Humanities and arts') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["Humanities and arts"].iloc[5:8]))

if (select_field == 'Other') & (select_feature == 'Citizenship (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[5:8],
                          y=data4["Other"].iloc[5:8]))




if (select_field == 'All fields') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["All fields"].iloc[9:11]))

if (select_field == 'Life sciencesa') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["Life sciencesa"].iloc[9:11]))

if (select_field == 'Physical sciences and earth sciences') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["Physical sciences and earth sciences"].iloc[9:11]))


if (select_field == 'Mathematics and computer sciences') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["Mathematics and computer sciences"].iloc[9:11]))

if (select_field == 'Psychology and social sciences') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["Psychology and social sciences"].iloc[9:11]))

if (select_field == 'Engineering') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["Engineering"].iloc[9:11]))


if (select_field == 'Education') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["Education"].iloc[9:11]))


if (select_field == 'Humanities and arts') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["Humanities and arts"].iloc[9:11]))

if (select_field == 'Other') & (select_feature == 'Marital status (%)'):
	fig5.add_trace(go.Bar(x=data4["Characteristic"].iloc[9:11],
                          y=data4["Other"].iloc[9:11]))

st.plotly_chart(fig5, use_container_width=True)
