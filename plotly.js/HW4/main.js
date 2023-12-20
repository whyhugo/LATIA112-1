let myGraph1 = document.getElementById('myGraph1');
let trace1 = {};
trace1.type = "bar";
trace1.title = "各年級用戶人數分布";
trace1.x = [];
trace1.y = [];
trace1.domain = {
    row:0,
    column:0
};

for (let i=0; i<user_grade.length; i++){
    trace1.x[i] = user_grade[i]['name'];
    trace1.y[i] = user_grade[i]['count'];
}


let myGraph2 = document.getElementById('myGraph2');
let trace2 = {};
trace2.type ="pie";
trace2.title = "老師與學生用戶比例";
trace2.labels = [];
trace2.values = [];
trace2.domain = {
    row:0,
    column:1
};
trace2.hole = 0.65;

for (let x=0; x<user_type.length; x++) {
    trace2.values[x] = user_type[x]['count'];
    trace2.labels[x] = user_type[x]['name'];
}

let myGraph3 = document.getElementById('myGraph3');
let trace3 = {};
trace3.mode = 'lines+markers';
trace3.type ="scatter";
trace3.title = "新用戶登入時間線";
trace3.x = [];
trace3.y = [];
trace3.domain = {
    row:1,
    column:0
};

for (let j=0; j<user_login.length; j++) {
    trace3.x[j] = user_login[j]['month'];
    trace3.y[j] = user_login[j]['count'];
}



let data1 = [];
data1.push(trace1);
let data2 = [];
data2.push(trace2);
let data3 = [];
data3.push(trace3);

let layout1 = {
    title: {
        text: '各年級用戶人數分布'
    },
    xaxis: {
        title: '年級'
    },
    yaxis: {
        title: '人數'
    },
    margin: {
        t: 70,
        l: 90
    }
};

let layout2 = {
    margin: {
        t: 70,
        l: 90
    }
};

let layout3 = {
    title: {
        text: '新用戶登入時間線'
    },
    xaxis: {
        title: '時間（年月）'
    },
    yaxis: {
        title: '新帳戶數量'
    },
    margin: {
        t: 70,
        l: 90
    }
};

Plotly.newPlot(myGraph1, data1, layout1);
Plotly.newPlot(myGraph2, data2, layout2);
Plotly.newPlot(myGraph3, data3, layout3);
