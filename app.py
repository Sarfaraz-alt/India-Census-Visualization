import streamlit as st
import data
import plotly.express as px

st.set_page_config(layout='wide')

st.sidebar.title("India Map")
selected_state = st.sidebar.selectbox('Select State',data.states)


primary = st.sidebar.selectbox('Select Primary Attribute',data.attributtes_)

secondary = st.sidebar.selectbox('Select Secondary Attribute',
                                 data.attributtes_)

l = data.attributtes_[-4:]
print(l)
plot = st.sidebar.button('Plot')

if plot:
    st.write('Primary Attribute is represented by Size')
    st.write('Secondary Attribute is represented by Color')

    if selected_state == 'All States':
        if secondary in l :
            st.plotly_chart(px.scatter_map(data.df, lat='Latitude', lon='Longitude',
                                   zoom=4,
                   color=secondary,size=primary,width=800,height=700,
                                   color_continuous_scale='Plasma_r',
                                   size_max=20,hover_name='District',
                                       hover_data={'Latitude':False,
                                                   'Longitude':False},
                                           range_color=(0,100)
                                       ),
                    use_container_width=True)
        else:
            st.plotly_chart(
                px.scatter_map(data.df, lat='Latitude', lon='Longitude',
                               zoom=4,
                               color=secondary, size=primary, width=800,
                               height=700,
                               color_continuous_scale='Plasma_r',
                               size_max=20, hover_name='District',
                               hover_data={'Latitude': False,
                                           'Longitude': False},
                               ),
                use_container_width=True)
    else:
        if secondary in l:
            st.plotly_chart(
                px.scatter_map(data.df, lat='Latitude', lon='Longitude',
                               zoom=4,
                               color=secondary, size=primary, width=800,
                               height=700,
                               color_continuous_scale='Plasma_r',
                               size_max=20, hover_name='District',
                               hover_data={'Latitude': False,
                                           'Longitude': False},
                               range_color=(0, 100)
                               ),
                use_container_width=True)
        else:
            st.plotly_chart(
                px.scatter_map(data.df, lat='Latitude', lon='Longitude',
                               zoom=4,
                               color=secondary, size=primary, width=800,
                               height=700,
                               color_continuous_scale='Plasma_r',
                               size_max=20, hover_name='District',
                               hover_data={'Latitude': False,
                                           'Longitude': False},
                               ),
                use_container_width=True)