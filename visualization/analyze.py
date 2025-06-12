import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, '..', 'data', 'cleaned_data.csv')

df = pd.read_csv(data_path)

# Create a subplot with 2 rows, specifying domain for pie chart
fig = make_subplots(
    rows=2, cols=1,
    subplot_titles=('Total Quantity Ordered By Product', 'Order Distribution by Status'),
    specs=[[{"type": "bar"}], [{"type": "domain"}]],
    vertical_spacing=0.2
)

# Bar Graph
product_quantity = df.groupby('PRODUCT')['QUANTITY'].sum().reset_index()

# Add bar chart
fig.add_trace(
    go.Bar(
        x=product_quantity['PRODUCT'],
        y=product_quantity['QUANTITY'],
        name='Product Quantity',
        marker_color='#FF69B4'  # Hot pink color
    ),
    row=1, col=1
)

# Pie Chart
status_counts = df['ORDERSTATUS'].value_counts()
fig.add_trace(
    go.Pie(
        labels=status_counts.index,
        values=status_counts.values,
        name='Order Status',
        hole=0.3,
        marker_colors=px.colors.qualitative.Pastel  # Pastel color palette
    ),
    row=2, col=1
)

# Create dropdown menu
fig.update_layout(
    height=1000,
    showlegend=True,
    title_text="Interactive Sales Dashboard",
    title_x=0.5,
    template="plotly_dark",  # Dark theme
    paper_bgcolor='#2B2B2B',  # Dark background
    plot_bgcolor='#2B2B2B',   # Dark background
    font=dict(color='white'),  # White text
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{"x": [product_quantity['PRODUCT']], "y": [product_quantity['QUANTITY']]}],
                    label="All Products",
                    method="restyle"
                ),
                *[
                    dict(
                        args=[{"x": [[product]], "y": [[product_quantity[product_quantity['PRODUCT'] == product]['QUANTITY'].iloc[0]]]}],
                        label=product,
                        method="restyle"
                    ) for product in product_quantity['PRODUCT']
                ]
            ]),
            direction="down",
            showactive=True,
            x=0.1,
            y=1.1,
            xanchor="left",
            yanchor="top"
        )
    ]
)

# Update axes
fig.update_xaxes(title_text="Product", row=1, col=1, gridcolor='#404040')
fig.update_yaxes(title_text="Total Quantity", row=1, col=1, gridcolor='#404040')

# Save as HTML for interactive viewing
fig.write_html("interactive_dashboard.html")

# Show in browser
fig.show()
