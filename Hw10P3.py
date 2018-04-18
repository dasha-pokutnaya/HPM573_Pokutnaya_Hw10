import InputDataHw10
import ParameterClassesHw10 as Settings
import scr.FormatFunctions as F

def print_comparative_outcomes(simOutputs_mono):
    """ prints average increase in survival time, discounted cost, and discounted utility
    under combination therapy compared to mono therapy
    :param simOutputs_mono: output of a cohort simulated under mono therapy

    """

    # increase in survival time under combination therapy with respect to mono therapy
    if Settings.Therapies.ANTICOAG:
        increase_survival_time = Stat.DifferenceStatPaired(
            name='Increase in survival time',
            x=simOutputs_combo.get_survival_times(),
            y_ref=simOutputs_mono.get_survival_times())
    else:
        increase_survival_time = Stat.DifferenceStatIndp(
            name='Increase in survival time',
            x=simOutputs_combo.get_survival_times(),
            y_ref=simOutputs_mono.get_survival_times())

    # estimate and CI
    estimate_CI = F.format_estimate_interval(
        estimate=increase_survival_time.get_mean(),
        interval=increase_survival_time.get_t_CI(alpha=Settings.ALPHA),
        deci=2)
    print("Average increase in survival time "
          "and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          estimate_CI)

    # increase in discounted total cost under combination therapy with respect to mono therapy
    if Settings.Therapies.ANTICOAG:
        increase_discounted_cost = Stat.DifferenceStatPaired(
            name='Increase in discounted cost',
            x=simOutputs_combo.get_costs(),
            y_ref=simOutputs_mono.get_costs())
    else:
        increase_discounted_cost = Stat.DifferenceStatIndp(
            name='Increase in discounted cost',
            x=simOutputs_combo.get_costs(),
            y_ref=simOutputs_mono.get_costs())

    # estimate and CI
    estimate_CI = F.format_estimate_interval(
        estimate=increase_discounted_cost.get_mean(),
        interval=increase_discounted_cost.get_t_CI(alpha=Settings.ALPHA),
        deci=0,
        form=F.FormatNumber.CURRENCY)
    print("Average increase in discounted cost "
          "and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          estimate_CI)

    # increase in discounted total utility under combination therapy with respect to mono therapy
    if Settings.Therapies.ANTICOAG:
        increase_discounted_utility = Stat.DifferenceStatPaired(
            name='Increase in discounted utility',
            x=simOutputs_combo.get_utilities(),
            y_ref=simOutputs_mono.get_utilities())
    else:
        increase_discounted_utility = Stat.DifferenceStatIndp(
            name='Increase in discounted cost',
            x=simOutputs_combo.get_utilities(),
            y_ref=simOutputs_mono.get_utilities())

    # estimate and CI
    estimate_CI = F.format_estimate_interval(
        estimate=increase_discounted_utility.get_mean(),
        interval=increase_discounted_utility.get_t_CI(alpha=Settings.ALPHA),
        deci=2)
    print("Average increase in discounted utility "
          "and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          estimate_CI)


def report_CEA_CBA(simOutputs_mono):
    """ performs cost-effectiveness analysis
    :param simOutputs_mono: output of a cohort simulated under mono therapy
    """

    # define two strategies
    mono_therapy_strategy = Econ.Strategy(
        name='Mono Therapy',
        cost_obs=simOutputs_mono.get_costs(),
        effect_obs=simOutputs_mono.get_utilities()
    )

    # CEA
    if Settings.Therapies.ANTICOAG:
        CEA = Econ.CEA(
            strategies=[mono_therapy_strategy, combo_therapy_strategy],
            if_paired=True
        )
    else:
        CEA = Econ.CEA(
            strategies=[mono_therapy_strategy, combo_therapy_strategy],
            if_paired=False
        )
    # show the CE plane
    CEA.show_CE_plane(
        title='Cost-Effectiveness Analysis',
        x_label='Additional discounted utility',
        y_label='Additional discounted cost',
        show_names=True,
        show_clouds=True,
        show_legend=True,
        figure_size=6,
        transparency=0.3
    )
    # report the CE table
    CEA.build_CE_table(
        interval=Econ.Interval.CONFIDENCE,
        alpha=Settings.ALPHA,
        cost_digits=0,
        effect_digits=2,
        icer_digits=2,
    )
