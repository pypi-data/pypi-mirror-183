import itertools

from gtnhvelo.gtnh.overclocks import OverclockHandler


class Graph:

    def __init__(self, graph_name, recipes, parent_context, graph_config=None, title=None):
        self.graph_name = graph_name
        self.recipes = {str(i): x for i, x in enumerate(recipes)}
        self.nodes = {}
        self.edges = {}  # uniquely defined by (machine from, machine to, ing name)
        self.parent_context = parent_context
        self.graph_config = graph_config
        self.title = title
        if self.graph_config == None:
            self.graph_config = {}

        # Populated later on
        self.adj = None
        self.adj_machine = None

        self._color_dict = dict()
        if self.graph_config.get('USE_RAINBOW_EDGES', None):
            self._color_cycler = itertools.cycle(self.graph_config['EDGECOLOR_CYCLE'])
        else:
            self._color_cycler = itertools.cycle(['white'])

        # Overclock all recipes to the provided user voltage
        oh = OverclockHandler(self.parent_context)
        for i, rec in enumerate(recipes):
            recipes[i] = oh.overclockRecipe(rec)
            rec.base_eut = rec.eut

        # DEBUG
        for rec in recipes:
            self.parent_context.cLog(rec)
        self.parent_context.cLog('')

    # Graph utility functions
    from ._utils import (
        userRound,
        addNode,
        addEdge,
        tierToVoltage,
        createAdjacencyList,
        _iterateOverMachines,
        _checkIfMachine,
    )
    userRound = staticmethod(userRound)

    # Setup of graph - connect edges and remove cycles
    from ._preProcessing import (
        connectGraph,
        removeBackEdges,
    )

    # Main runtime - describes primary behavior
    from ._core import (
        balanceGraph,
        outputGraphviz
    )

    # Machine locking - core autobalancing functionality
    from ._machineLocking import (
        _lockMachine,
        _lockMachineEdges,
        _simpleLockMachineEdges,
    )

    # Utilities for "port node" style graphviz nodes
    from ._portNodes import (
        stripBrackets,
        nodeHasPort,
        getOutputPortSide,
        getInputPortSide,
        getUniqueColor,
        getPortId,
        getIngId,
        getIngLabel,
        getQuantLabel,
        _combineInputs,
        _combineOutputs,
    )

    # Add summary and power burning machines
    from ._postProcessing import (
        _addSummaryNode,
        _addPowerLineNodes,
        bottleneckPrint,
    )
