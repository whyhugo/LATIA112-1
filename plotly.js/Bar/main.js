let myGraph = document.getElementById('myGraph');
let trace1 = {};
trace1.type = "bar";
trace1.name = "lion"
trace1.x = ['Taipei Zoo','Tauyuan Zoo'];
trace1.y = [animals_Taipei_Zoo[0]['count'], animals_Taoyuan_Zoo[0]['count']];

//for (let i=0; i<animals_Taipei_Zoo.length; i++) {
//    trace1.y[0] = animals_Taipei_Zoo[0]['count'];
//    trace1.y[1] = animals_Taoyuan_Zoo[0]['count'];
//}

trace1.text = trace1.y;
trace1.textfont = {
    size:16,
    color:'white'
}
trace1.marker = {
    //color: ""
}

let trace2 = {};
trace2.type = "bar";
trace2.name = "tiger"
trace2.x = ['Taipei Zoo','Tauyuan Zoo'];
trace2.y = [animals_Taipei_Zoo[1]['count'], animals_Taoyuan_Zoo[1]['count']];;

//for (let i=0; i<animals_Taoyuan_Zoo.length; i++) {
//    trace2.y[0] = animals_Taipei_Zoo[1]['count'];
//    trace2.y[1] = animals_Taoyuan_Zoo[1]['count'];
//}

trace2.text = trace2.y;
trace2.textfont = {
    size:16,
    color:'white'
}
trace2.marker = {
    //color: ""
}

let trace3 = {};
trace3.type = "bar";
trace3.name = "monkey";
trace3.x = ['Taipei Zoo','Tauyuan Zoo'];
trace3.y = [animals_Taipei_Zoo[2]['count'], animals_Taoyuan_Zoo[2]['count']];;

//for (let i=0; i<animals_Taipei_Zoo; i++) {
//    trace3.y[0] = animals_Taipei_Zoo[2]['count'];
//    trace3.y[1] = animals_Taoyuan_Zoo[2]['count'];
//}

trace3.text = trace3.y;
trace3.textfont = {
    size:16,
    color:'white'
}
trace3.marker = {
    //color: ""
}

let data = [];
data.push(trace1);
data.push(trace2);
data.push(trace3);

let layout = {
    margin:{
        t:0
    },
    barmode: 'stack'
};

Plotly.newPlot(myGraph, data, layout);

