from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask_appbuilder.charts.views import DirectByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Tabulka
from . import appbuilder, db


class CountryDirectChartView(DirectByChartView):
    datamodel = SQLAInterface(Tabulka)
    chart_title = 'Direct Data Example'

    definitions = [
        {
            'label': 'cislo',
            'group': 'id',
            'series': ['cislo',
                       'id']
        }
    ]


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
appbuilder.add_view(CountryDirectChartView, "Graf", category="Statistics")