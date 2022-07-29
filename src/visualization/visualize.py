import plotly.graph_objects as go


def create_figure(data, base_currency):
    fig = go.Figure()

    # Draw points
    fig.add_trace(
        go.Scatter(
            y=data[base_currency],
            x=data["name"],
            mode='markers',
            marker_color='darkblue',
            marker_size=10,
        )
    )

    # Draw lines
    for i in range(0, len(data)):
        fig.add_shape(
            type='line',
            y0=0,
            x0=i,
            y1=data[base_currency][i],
            x1=i,
            line=dict(
                color='crimson' if data[base_currency][i] < 0 else 'blue', width=3
            ),
        )

    # Set x-axes tick mode
    fig.update_xaxes(
        tickmode='linear',
        showgrid=False,
        fixedrange=True,
        tickfont=dict(family="arial", size=6),
    )

    # Set y-axes as percentage
    fig.update_yaxes(tickformat=".1%", showgrid=False, fixedrange=True)

    # Set figure size
    fig.update_layout(
        autosize=False,
        margin=dict(l=0, r=0, t=0, b=0),
        width=700,
        height=500,
        plot_bgcolor="rgba(255,255,255,1)",
    )
    return fig
