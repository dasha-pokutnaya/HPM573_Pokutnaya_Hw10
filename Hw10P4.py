import SupportMarkovModelHw10
import InputDataHw10
import ParameterClassesHw10 as Settings
import scr.FormatFunctions as F
import scr.EconEvalClasses as Econ

# CBA
    if Settings.Therapies.ANTICOAG:
        NBA = Econ.CBA(
            strategies= Settings.Therapies.ANTICOAG,
            if_paired=True
        )
    else:
        NBA = Settings.Therapies.NONE

    # show the net monetary benefit figure
    NBA.graph_deltaNMB_lines(
        min_wtp=0,
        max_wtp=50000,
        title='Cost-Benefit Analysis',
        x_label='Willingness-to-pay for one additional QALY ($)',
        y_label='Incremental Net Monetary Benefit ($)',
        interval=Econ.Interval.CONFIDENCE,
        show_legend=True,
        figure_size=6
    )

# Unfortunately I was not able to answer the question because my code did not run.