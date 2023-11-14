//get csv file
d3.csv('data/harry_potter.csv').then(
    res => {
        console.log('Local CSV:', res)
    }
);
//get json file
d3.json('data/harry_potter.json').then(
    res => {
        console.log('Local json:', res)
    }
);


let myGraph = document.getElementById('myGraph');

let trace1 = {};
trace1.mode = "markers";
trace1.type = "scatter";
trace1.x = [];
trace1.y = [];
trace1.text = [];

for (let i = 0; i < set1.length; i++) {
    trace1.x[i] = res[i]["release_year"];
    trace1.y[i] = res[i]["revenue"];
    trace1.text[i] = res[i]["title"];
}

let trace2 = {};
trace2.mode = "lines";
trace2.type = "scatter";
trace2.x = [];
trace2.y = [];

for (let i = 0; i < set2.length; i++) {
    trace2.x[i] = set2[i][0];
    trace2.y[i] = set2[i][1];
}

let trace3 = {};
trace3.mode = "lines + markers";
trace3.type = "scatter";
trace3.x = [];
trace3.y = [];

for (let i = 0; i < set3.length; i++) {
    trace3.x[i] = set3[i][0];
    trace3.y[i] = set3[i][1];
}

let data = [];
data.push(trace1);
data.push(trace2);
data.push(trace3);

let layout = {
    margin: {
        t:0
    }
};

Plotly.newPlot(myGraph, data, layout)