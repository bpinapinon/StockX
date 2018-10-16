//d3.json("/bubble", function (buildBubble) {
var url = `/bubble`

function buildBubble() {

    

    d3.json(url).then(function(response){
        console.log(response);

        var trace = {
            x: response.map(sneakers => sneakers.Retail_Price),
            y: response.map(sneakers => sneakers.Avg_Sale_Price),
            mode: "markers",
            type: "scatter",
            hovertext: response.map(sneakers => sneakers.Model),
            marker: {
            size: response.map(sneakers => sneakers.Number_of_Sales),
            color: response.map(sneakers => sneakers.Color),
            sizemode:'area'
      //sizeref: 2.*max(size)/(40.**2),
      //sizemin: 4
      //colorscale: "Earth"
            };
        };

        var data = [trace];

        var layout = {
            title: "Bubble Plot",
            xaxis: {title: "Retail Price ($)"},
            yaxis: {title: "Average Sale Price ($)"},
            hovermode: 'closest'
        };

        Plotly.newPlot("bubble", data, layout);

    });

};
//buildBubble();


