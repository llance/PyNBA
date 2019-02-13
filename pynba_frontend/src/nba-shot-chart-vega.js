import React from 'react'
import ReactDOM from 'react-dom'
import d3 from 'd3'
import vg from 'vega'
import { ShotChartSpec } from './components/basketball'

// harden 201935
// curry 201939
// kobe 977
// lebron 2544
// korver 2594
// klay 202691
// westbrook 201566
// durant 201142
// dirk 1717
// rose 201565
// anthony davis 203076

// http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID=&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=

class NBAShotChart{
    constructor(){
        this.ShotChartView = null;
        this.Cache = {};
        this.shotChartUrls = [
            {"name": "James Harden (2014-2015)",  "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/5c74a5dcd7b257faa985f28c932a684ed4cea065/james-harden-shotchartdetail.json", "dash_url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/f6d6496474af6dfba0b73f36dbd0e00ce0fc2f42/james-harden-2014-2015-player-dash.json"},
            {"name": "Stephen Curry (2014-2015)", "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/d159840109c00928f515bf0ed496f4f487b326ba/stephen-curry-shotchartdetail.json" },
            {"name": "Kobe Bryant (2007-2008)",   "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/0fbd65f9f795a5fba8c8ccefce060fd3082264fb/kobe-2007-2008-shot-chart.json" },
            {"name": "Kobe Bryant (2009-2010)",   "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/a19ec840d7d67c388fc3f2eea3d51c9b7cdcf4b0/kobe-2009-2010-shot-chart.json" },
            {"name": "Lebron James (2009-2010)",  "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/0fbd65f9f795a5fba8c8ccefce060fd3082264fb/lebron-james-2009-2010-shot-chart.json" },
            {"name": "Lebron James (2010-2011)",  "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/0fbd65f9f795a5fba8c8ccefce060fd3082264fb/lebron-james-2010-2011-shot-chart.json" },
            {"name": "Lebron James (2011-2012)",  "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/d53dbb96502622b9509880fb671cf50846130636/lebron-james-2011-2012-shot-chart.json" },
            {"name": "Lebron James (2012-2013)",  "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/d53dbb96502622b9509880fb671cf50846130636/lebron-james-2012-2013-shot-chart.json" },
            {"name": "Kevin Durant (2013-2014)",  "url": "https://gist.githubusercontent.com/sandbox/7f6065c867a5f355207e/raw/d53dbb96502622b9509880fb671cf50846130636/kevin-durant-2013-2014-shot-chart.json" }
        ]
        var self = this;

        vg.parse.spec(ShotChartSpec, function(chart) {
            console.log('ShotChartSpec', ShotChartSpec);
            self.ShotChartView = chart({el: "#shot-chart"});
            self.ShotChartView.onSignal('minchartX', (signal, value) => console.log(signal, value))
            self.ShotChartView.onSignal('maxchartX', (signal, value) => console.log(signal, value))
            // console.log('this.shotChartUrls[0].url', self.shotChartUrls)
            // console.log('self is ', self);
            self.renderShotChart({ target: { value: self.shotChartUrls[0].url }})
        })
    }

    setChartData(data, self) {
        console.log('self in setChartData is ', self, 'data is ', data);
        self.ShotChartView.data('table').remove(() => true).insert(data)
        // self.ShotChartView.update({duration: 300, ease: "quad-in-out"})
        console.log(self.ShotChartView.toImageURL('png'))
    };

    renderShotChart(evt) {
        var self = this;
        console.log('self in rendershotchart is ', self)
        let url = evt.target.value
        if (Cache[url]) {
            this.setChartData(Cache[url])
        } else {
            d3.json(
                url,
                function(error, json) {
                    if (error) return console.warn(error)
                    let headers = json.resultSets[0].headers
                    let data = json.resultSets[0].rowSet.map(function(d) {
                        let row = headers.reduce(function(memo, header, i) {
                            memo[header] = d[i]
                            return memo
                        }, {})
                        row.shot_id = `${row.GAME_ID}_${row.GAME_EVENT_ID}`
                        return row})
                    self.Cache[url] = data
                    self.setChartData(self.Cache[url], self)
                })
        }
    };

    render(){
        ReactDOM.render(<select onChange={this.renderShotChart}>
            {this.shotChartUrls.map(function(player) {
                return <option key={player.url} value={player.url}>{player.name}</option>
            })}
        </select>, document.getElementById("shot-chart-player-select"))
    };
}

export default NBAShotChart;
