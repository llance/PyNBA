import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import d3 from './js/d3.js'


class App extends Component {
    constructor(props) {
        super(props)
        this.handleClick = this.handleClick.bind(this)
        var courtSelection = d3.select("#shot-chart");
        var court = d3.court().width(600);
        var shots = d3.shots().shotRenderThreshold(1).displayToolTips(true).displayType("hexbin");
        courtSelection.call(court);
        courtSelection.datum(data).call(shots);
    }


    render () {
        return (
            <div className='button__container'>
                <button className='button' onClick={this.handleClick}>
                    Click Me
                </button>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.4.0/d3.min.js"></script>
                <script src="https://d3js.org/d3-hexbin.v0.2.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/d3-tip/0.7.1/d3-tip.min.js"></script>
                <script src="d3-shotchart.js" ></script>
                <script src="shots.js" ></script>

            </div>

        )
    }

    componentDidMount() {
        var xhr = new XMLHttpRequest();
        var json_obj, status = false;
        xhr.open("GET", "https://jsonplaceholder.typicode.com/photos/", true);
        xhr.onload = function (e) {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    var json_obj = JSON.parse(xhr.responseText);
                    status = true;
                    this.setState({ json_obj });
                } else {
                    console.error(xhr.statusText);
                }
            }
        }.bind(this);
        xhr.onerror = function (e) {
            console.error(xhr.statusText);
        };
        xhr.send(null);
    }


    handleClick () {
        console.log('hello')
        var xhr = new XMLHttpRequest()
        xhr.open("GET", 'http://127.0.0.1:8000/playershotchart/2544/', true)
        // xhr.setRequestHeader('Access-Control-Allow-Origin', '*')
        // xhr.setRequestHeader("Access-Control-Allow-Credentials", "true");
        // xhr.setRequestHeader("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
        // xhr.setRequestHeader("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers")

        xhr.onload = function(e){
            if (xhr.readyState === 4){
                if (xhr.status === 200){
                    console.log(xhr.response)
                } else {
                    console.error(xhr.statusText)
                }
            }
        }.bind(this)
        xhr.onerror = function(e){
            console.error(xhr.statusText)
        }
        xhr.send(null)


    }
}

export default App;
