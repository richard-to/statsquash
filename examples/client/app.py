from flask import Flask, render_template

import StatSquash.config as config
import StatSquash.recipes as recipes
from StatSquash.client import GrapherChef, MySqlHarvester, GoogleChartStyle

app = Flask(__name__)
app.debug = True

@app.route('/')
def demo():
    harvester = MySqlHarvester(config.load_db, config.tables['monthly'])
    style = GoogleChartStyle()

    chef = GrapherChef(harvester, style)
    graphs = chef.cook(recipes.cookbook)

    return render_template("demo_chart.html", graphs=graphs)

if __name__ == '__main__':
    app.run()