import importlib
from typing import Union

import pandas as pd
from assertpy import assert_that

from deepdriver.sdk.chart.chart import Chart, TYPE_CONFUSION_MATRIX
from deepdriver.sdk.data_types.image import Image
from deepdriver.sdk.data_types.table import Table


def visualize(obj: Union[Chart, Table, Image]) -> None:
    assert_that(obj).is_not_none()

    if isinstance(obj, Chart):
        if obj.chart_type == TYPE_CONFUSION_MATRIX:
            # dataframe 에서 x, y, z 값 추출
            actual = obj.data.dataframe['Actual']
            predicted = obj.data.dataframe['Predicted']
            n_redictions = obj.data.dataframe['nPredictions']
            cross_tab_df = pd.crosstab(index=actual, columns=predicted, values=n_redictions, aggfunc=sum)
            labels, z = [], []
            for item in cross_tab_df.iteritems():
                # item : ('cat', 'list[]')
                labels.append(item[0])
                z.append(list(item[1]))

            # 그래프 그리기
            plotly_path = "plotly.graph_objects"
            plotly_module = importlib.import_module(plotly_path)
            data = plotly_module.Heatmap(z=z, x=labels, y=labels)
            annotations = []
            for i, row in enumerate(z):
                for j, value in enumerate(row):
                    annotations.append(
                        {
                            "x": labels[i],
                            "y": labels[j],
                            # "font": {"color": "white"},
                            "text": str(value),
                            "xref": "x1",
                            "yref": "y1",
                            "showarrow": False
                        }
                    )
            layout = {
                "title": obj.label_fields["title"],
                "xaxis": {"title": "Predicted"},
                "yaxis": {"title": "Actual"},
                "annotations": annotations
            }
            fig = plotly_module.Figure(data=data, layout=layout)
            fig.show()
        else:
            # historgram, line, scatter 차트
            plotly_path = "plotly.express"
            plotly_module = importlib.import_module(plotly_path)
            plotly_chart_func = getattr(plotly_module, obj.chart_type)

            fig = plotly_chart_func(
                x=obj.data.dataframe[obj.data_fields["x"]],
                y=obj.data.dataframe[obj.data_fields["y"]],
                labels=obj.data_fields,
                title=obj.label_fields["title"],
            )
            fig.show()
    elif isinstance(obj, Table):
        # from IPython.core.display import display, HTML
        # display(HTML(obj.data.dataframe._repr_html_()))

        plotly_path = "plotly.graph_objects"
        plotly_module = importlib.import_module(plotly_path)

        fig = plotly_module.Figure(
            data=[plotly_module.Table(
                header=dict(values=obj.data.columns),
                cells=dict(values=obj.data.dataframe.T))
            ],
        )
        fig.show()
    elif isinstance(obj, Image):
        # from IPython.core.display import display, HTML
        # display(HTML(obj.data.dataframe._repr_html_()))

        plotly_path = "plotly.express"
        plotly_module = importlib.import_module(plotly_path)
        import numpy as np
        fig = plotly_module.imshow(
            np.array(obj.data)
        )
        fig.show()
