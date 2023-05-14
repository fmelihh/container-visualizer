import plotext as plt
from typing import List, Any


def line_chart(
        title: str,
        x_axis: List[int],
        y_axis: List[int],
        date_form: List[str],
        x_axis_lower_limit: Any,
        x_axis_upper_limit: Any,
        y_axis_lower_limit: Any,
        y_axis_upper_limit: Any,
        color: str = "red",
):
    plt.clt()
    plt.clc()
    plt.title(title)
    plt.date_form(date_form[0], date_form[1])
    plt.ylim(y_axis_lower_limit, y_axis_upper_limit)
    plt.xlim(x_axis_lower_limit, x_axis_upper_limit)
    plt.plot(
        x_axis,
        y_axis,
        color=color,
    )
    plt.show()
    plt.sleep(0.1)

