var trace = {
    x: adidas.map(row => row.Retail_Price),
    y: adidas.map(row => row.Avg_Sale_Price),
    mode: "markers",
    type: "scatter",
    hovertext: adidas.map(row => row.Model),
    marker: {
      size: adidas.map(row => row.Number_of_Sales),
      color: adidas.map(row => row.Color),
      sizemode:'area',
      //sizeref: 2.*max(size)/(40.**2),
      //sizemin: 4
      //colorscale: "Earth"
    },
};

var data = [trace]

var layout = {
    title: "Bubble Plot",
    xaxis: {title: "Retail Price ($)"},
    yaxis: {title: "Average Sale Price ($)"},
    hovermode: 'closest'
};

Plotly.newPlot("bubble", data, layout);
