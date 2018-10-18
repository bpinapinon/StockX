var url = "/bubbledata";


function buildPlot() {
    d3.json(url).then(function(error, response) {

        console.log(response);

        //var sneakers = [response];

        var trace = {
            mode: "markers",
            type: "scatter",
            x: response.map(sneakers => sneakers.retailPrice),
            y: response.map(sneakers => sneakers.avgSalePrice), 
            hovertext: response.map(sneakers => sneakers.brand),
            marker: {
            size: response.map(sneakers => sneakers.noSales),
            color: response.map(sneakers => sneakers.color),
            sizemode:'area'
            }
        };

        var data = [trace];

        var layout = {
            title: "Bubble Plot",
            xaxis: {title: "Retail Price ($)"},
            yaxis: {title: "Average Sale Price ($)"},
            hovermode: "closest"
        };

    Plotly.plot("bubble", data, layout);
    });
}
buildPlot();
