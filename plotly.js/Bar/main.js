letmyGraph = document.getElementById('myGraph');
let trace1 = {};
trace1.type = "bar";
trace1.x = [];
trace1.y = [];
for (let i=0; i<animals.length; i++) {
    trace1.x[i] = animals[i]['name'];
    trace1.y[i] =animals[i]['count'];
}

let data = [];
data.push(trace1);

let layout = {
    margin:{t:0}
};

Plotly.newPlot(myGraph, data, layout);

