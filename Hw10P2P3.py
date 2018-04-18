import InputDataHw10
import ParameterClassesHw10 as Settings
import scr.FormatFunctions as F

def print_comparative_outcomes(simOutputs_mono):
    """ prints average increase in survival time, discounted cost, and discounted utility
    under combination therapy compared to mono therapy
    :param simOutputs_mono: output of a cohort simulated under mono therapy

    """

    # increase in survival time under coagulation therapy
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

    # increase in discounted total cost under coagulation therapy
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

    # increase in discounted total utility under coagulation therapy
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
