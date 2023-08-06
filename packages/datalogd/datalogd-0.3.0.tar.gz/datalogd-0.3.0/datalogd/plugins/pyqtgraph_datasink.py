import logging
import re
from datetime import datetime, timezone
from multiprocessing import Process, Queue
from queue import Empty

from datalogd import DataSink, listify

try:
    from PySide6 import QtCore
    from PySide6 import QtWidgets

    import pyqtgraph as pg
except ModuleNotFoundError:
    log = logging.getLogger(__name__.rpartition(".")[2])
    log.warning("pyqtgraph module not found. Install it with \"pip install pyqtgraph pyside6\" or similar.")
else:
    # Required modules present, continue loading rest of this module
    import numpy as np


    class PyqtgraphDataSink(DataSink):
        """
        Plot data in realtime in a pyqtgraph window.

        Multiple plot areas may be defined which will be stacked in rows with (by default) linked
        time axes. Each plot area may itself have multiple traces contained within. The complete
        plot configuration is defined in the initialisation parameters. The data to use for each
        trace is selected by matching a series of key-value pairs, in a similar manner to the
        :data:`~datalogd.plugins.keyval_datafilter.KeyValDataFilter`.

        A limited number of data points are stored to be plotted, after which the oldest data points
        will be discarded to make way for incoming data. The number of data points can be specified
        with the ``npoints`` parameter, with a default of 2048.

        The plot layout is described by the ``plotlayout`` parameter. As python code:

        .. code-block:: python

            plotlayout = [
                # List of plot panels
                {
                    # Plot 1 panel definition
                    'ylabel': 'Value (a.u)',
                    'traces': [
                        # List of trace definitions for this plot panel
                        {
                            # Trace 1 definition
                            'name': 'Trace 1',
                            'pen': [255, 255, 0],
                            'selector': [
                                # list of key-value pairs to match to data (same as KeyValDataFilter)
                                ['type', 'analog'],
                                ['id', '.*0']
                            ]
                        }, # ... possibly more trace definitions
                    ]
                }, # ... possibly more plot definitions
            ]
        
        In the connection graph configuration the ``plotlayout`` data structure must be a string
        formatted as JSON.

        Note that any fields present in a trace definition (such as ``'name'`` and ``'pen'``) are
        passed to the pyqtgraph :data:`~pyqtgraph.graphicsItems.PlotDataItem` initialisation which
        may be used to customise the trace, such as defining line color or changing to a scatter
        plot.

        Passing the parameter ``xlink=False`` will unlink the time axes of the plots, so changes to
        the view of one plot will not affect the others..

        Any additional parameters are passed to the pyqtgraph
        :data:`~pyqtgraph.widgets.GraphicsLayoutWidget` initialisation, which can be used to
        customise the plot window. For example, changing the window title and size with
        ``title="Plots"`` and ``size=[1000, 600]``.

        :param npoints: Maximum number of data points for a trace.
        :param title: String for title of the plot window.
        :param size: Tuple of (height, width) of the plot window.
        :param plotlayout: Data structure describing the plot layout and traces.
        :param xlink: Boolean, link the time axes of the plots.
        """
        def __init__(self, **kwargs):
            
            self.q = Queue()
            kwargs.update({"data_queue": self.q})
            self.appprocess = Process(target=self._exec_qt_app, kwargs=kwargs, name="PlotWindow")
            self.appprocess.start()

        def close(self):
            """
            Signal the pyqtgraph application to close when the application is shutting down.
            """
            #print("Waiting for QApplication to close...")
            self.appprocess.terminate()
            self.appprocess.join()
            #print("QApplication closed.")

        def receive(self, data):
            """
            Accept the provided ``data`` and pass it to the pyqtgraph :data:`PlotWindow` for
            display.
            """
            if self.appprocess.is_alive():
                data = listify(data)
                self.q.put(data)

        def _exec_qt_app(self, **kwargs):
            self.plotwindow = PlotWindow(**kwargs, show=True)
            app = QtWidgets.QApplication.instance()
            app.exec()


    class PlotWindow(pg.GraphicsLayoutWidget):

        def __init__(self, parent=None, data_queue=None, npoints=2**11, plotlayout=None, xlink=True, **kwargs):
            super().__init__(**kwargs)
            
            # Queue object for receiving data through
            self.data_queue = data_queue

            # Default plot layout if none specified
            if plotlayout is None: plotlayout = [{}]
            if not type(plotlayout) == list:
                raise RuntimeError(f"plotlayout should be a list of dicts, not \"{type(plotlayout).__name__}\"")

            pg.setConfigOption("antialias", True)

            # Parse plot layout data structure to construct plots
            # The data structure looks like:
            # self.plots = [
            #   (PlotItem, [
            #     (PlotDataItem, tracedata, [
            #       ('selector1key', 'selector1value'),
            #       ('selector2key', 'selector2value'), ... more data selection criteria
            #     ]), ... more traces inside this plot
            #   ), ... more plot panels
            # ]
            self.plots = []
            for pl in plotlayout:
                p = self._get_plot_defaults()
                p.update(pl)
                plot = self.addPlot(bottom="Time (s)", left=p["ylabel"])
                plot.setAxisItems({"bottom": pg.DateAxisItem()})
                plot.showGrid(x=True, y=True)
                plot.addLegend()
                if xlink and len(self.plots) > 0:
                    plot.setXLink(self.plots[0][0])
                traces = []
                for t in p["traces"]:
                    traceaxis = np.full(npoints, np.nan)
                    tracedata = np.full(npoints, np.nan)
                    # Remove selector from dictionary, pass key/value pairs as params to plot init method
                    selector = t.pop("selector")
                    trace = plot.plot(**t)
                    traces.append((trace, traceaxis, tracedata, selector))
                self.plots.append((plot, traces))
                self.nextRow()


            if not self.data_queue is None:
                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self._update_plot)
                self.timer.start(15)


        def _get_plot_defaults(self):
            return {
                "ylabel": "Value (a.u.)",
                "traces": [{
                    "name": "Trace 1",
                    "pen": (255, 255, 255),
                    "selector": [
                        ["type", ".*"],
                    ]
                }]
            }


        def _update_plot(self):
            while not self.data_queue.empty():
                try:
                    data = self.data_queue.get(timeout=0.05)
                except queue.Empty:
                    return
                for d in data:
                    # Look through plot trace selector criteria looking for matching data
                    for p in self.plots:
                        for t in p[1]:
                            trace = t[0]
                            traceaxis = t[1]
                            tracedata = t[2]
                            selectors = t[3]
                            # Start by assuming data matches the selection criteria
                            match = True
                            try:
                                # Loop through each selection criteria
                                for s_k, s_v in selectors:
                                    # Try looking for this key in this data entry
                                    v = d[s_k]
                                    # This key exists, check its value
                                    if s_v == v or ((type(s_v) == type(v) == str) and re.fullmatch(s_v, v)) or s_v is NotImplemented:
                                        # Value matches this trace so far, keep checking any remaining selection criteria
                                        continue
                                    else:
                                        # Value doesn't match this trace, can stop checking now
                                        match = False
                                        break
                            except (IndexError, KeyError, ValueError) as ex:
                                # An exception means we couldn't match this data entry to this trace
                                print(ex)
                                match = False
                            if match and "value" in d:
                                # This data entry matched the selection criteria for this trace, update it
                                tracedata[0:-1] = tracedata[1:]
                                tracedata[-1] = d["value"]
                                # Get timestamp from data, or create one if it doesn't exist
                                traceaxis[0:-1] = traceaxis[1:]
                                try:
                                    traceaxis[-1] = d["timestamp"].timestamp()
                                except:
                                    traceaxis[-1] = datetime.now().timestamp()
                                trace.setData(x=traceaxis, y=tracedata)


