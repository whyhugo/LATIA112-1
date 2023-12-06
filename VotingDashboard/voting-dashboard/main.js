let myGraph = document.getElementById('myGraph');
let myGraph2 = document.getElementById('myGraph2');
let myGraph3 = document.getElementById('myGraph3');
let myGraph4 = document.getElementById('myGraph4');

d3.json(dataURL).then(getJSON_data);

function unpack(rows, key){
    return rows.map(function(row){
        return row[key];
    });
}

function getJSON_data(rows){
    console.log(rows);
    console.log(unpack(rows, "gender"));
    let trace1 = {};
    trace1.type = "pie";
    trace1.title = "性別";
    trace1.labels = ["男生","女生","不願透露"];
    trace1.values = [];
    trace1.hole = 0.5;

    trace1.values[0] = 0;
    trace1.values[1] = 0;
    trace1.values[2] = 0;
    for(let x=0; x<rows.length; x++){
        if(rows[x]['gender']=="Male"){
            trace1.values[0] += 1;
        } else if (rows[x]['gender'] == "Female"){
            trace1.values[1] += 1;
        }else{
            trace1.values[2] += 1;
        }
    }

    let trace2 = {};
    trace2.type = "histogram";
    trace2.title = "年齡";
    trace2.x = unpack(rows, "age");

    let trace3 = {};
    trace3.type = "scattermapbox";
    trace3.title = "居住地區";
    trace3.text = [];
    trace3.lat = unpack(city_location, "lat");
    trace3.lon = unpack(city_location, "lon");
    trace3.marker = {
        color:'blue',
        size:[]
    };

    for(let i=0;i<city_location.length;i++){
        trace3.text[i] = 0;
    }

    for(let i=0;i<rows.length;i++){
        for(let j=0;j<city_location.length;j++){
            if(rows[i]['area'] == city_location[j]['name']){
                trace3.text[j]+=1;
            }
        }
    }

    for (let i = 0; i < city_location.length; i++) {
        trace3.marker.size[i] = trace3.text[i]*10;
    }
    
    console.log(trace3.text);
    let trace4 = {};
    trace4.type = "bar";
    trace4.title = "颱風天夜晚的食物方案";
    trace4.x = ["出去吃","叫外送","自己煮"];
    trace4.y = [];

    for (let i = 0; i < trace4.x.length; i++) {
        trace4.y[i] = 0;
    }

    for (let i = 0; i < rows.length; i++) {
        trace4.y[rows[i]['food']] += 1;
    }

    console.log(trace4.x);
    console.log(trace4.y);

    let data = [];
    data.push(trace1);

    let data2 = [];
    data2.push(trace2);

    let data3 = [];
    data3.push(trace3);

    let data4 = [];
    data4.push(trace4);

    let layout = {
        margin:{
            t:10,
            l:10
        }
    };

    let layout2 = {
        margin: {
            t: 10,
            l: 10
        }
    };

    let layout3 = {
        margin: {
            t: 10,
            l: 10
        },
        dragmode:"zoom",
        mapbox:{
            style:"open-street-map",
            center:{
                lat: 23.708167, 
                lon: 120.929999
            },
            zoom:5.5
        }
    };

    let layout4 = {
        margin: {
            t: 10,
            l: 10
        }
    };

    Plotly.newPlot(myGraph, data, layout);
    Plotly.newPlot(myGraph2, data2, layout2);
    Plotly.newPlot(myGraph3, data3, layout3);
    Plotly.newPlot(myGraph4, data4, layout4);
    
}