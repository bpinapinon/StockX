function buildBubble() {

var url = `/bubble`
d3.json(url).then(function(sneaker_data){
    var trace = {
        x: sneaker_data.map(row => row.Retail_Price),
        y: sneaker_data.map(row => row.Avg_Sale_Price),
        mode: "markers",
        type: "scatter",
        hovertext: sneaker_data.map(row => row.Model),
        marker: {
        size: sneaker_data.map(row => row.Number_of_Sales),
        color: sneaker_data.map(row => row.Color),
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

})
}