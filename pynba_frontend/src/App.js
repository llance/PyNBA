import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'

const queryString = require('query-string');

class App extends Component {
    render () {
        return (
            <div className='button__container'>
                <button className='button' onClick={this.handleClick}>
                    Click Me
                </button>
                <p>{this.state.username}</p>
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

    constructor () {
        super()
        this.state = {
            username: ''
        }
        this.handleClick = this.handleClick.bind(this)
    };


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
